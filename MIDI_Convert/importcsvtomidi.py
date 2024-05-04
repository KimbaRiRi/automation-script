import csv
import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage
import logging

logger = logging.getLogger(__name__)

def convert_csv_to_midi(input_file, output_file, bpm):
    # Create a new MIDI file with a single track
    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)

    # Set tempo based on BPM
    ticks_per_beat = midi_file.ticks_per_beat
    ticks_per_second = ticks_per_beat * bpm / 60

    tempo_message = MetaMessage('set_tempo', tempo=mido.bpm2tempo(bpm))
    track.append(tempo_message)

    last_tick = 0
    max_tick = 0  # Track the maximum tick value
    drum_mapping = {
        'crash': 49,
        'hihat_c': 42,
        'kick_drum': 36,
        'ride': 51,
        'snare': 38,
        'tom_h': 47
                # Add more mappings if needed
    }

    # Read data from the CSV file
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            prediction = float(row['prediction'])
            time = float(row['time'])
            # confidence = float(row['confidence']).strip('%') / 100.0
            
            if drum_type in drum_mapping:
                note = drum_mapping[drum_type]
            # Convert the time in seconds to ticks
            current_tick = int(round(time * ticks_per_second))
            delta = current_tick - last_tick

            # Update max_tick
            max_tick = max(max_tick, current_tick)

            # Add a note_on event
            # track.append(Message('note_on', note=int(prediction * 127), velocity=64, time=delta, channel=9))

            # Add a note_off event (you may want to adjust the duration)
            # track.append(Message('note_off', note=int(prediction * 127), velocity=64, time=int(round(0.015*ticks_per_second)), channel=9))
            
            # Add a note_on event
            track.append(Message('note_on', note=note, velocity=64, time=delta, channel=9))
            # Add a note_off event (you may want to adjust the duration)
            track.append(Message('note_off', note=note, velocity=64, time=int(round(0.015*ticks_per_second)), channel=9))

            last_tick = current_tick

    # Set the end of the track based on the maximum tick value
    track.append(MetaMessage('end_of_track', time=max_tick))

    # Get the length of the MIDI file in seconds
    song_length = max_tick / ticks_per_second

    # Print the song length
    print(f"Song length: {song_length} seconds")

    # Save the converted MIDI file
    midi_file.save(output_file)

# Example usage
input_file = "./Music/DrumTranscriber-main/midi/Plave_6thSummerPaperdoll.csv"  # Replace with your CSV file path
output_file = "midi/Plave_6thSummerPaperdoll.mid"
bpm = 90  # Set your desired BPM

convert_csv_to_midi(input_file, output_file, bpm)
print(f"Converted MIDI file saved to: {output_file}")

logger.info("Converted MIDI file saved to: %s", output_file)
