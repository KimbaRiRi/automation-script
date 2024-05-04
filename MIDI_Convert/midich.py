import mido

def convert_to_percussion_midi(input_file, output_file):
  """Converts a MIDI file to percussion format (channel 10).

  Args:
      input_file: Path to the input MIDI file.
      output_file: Path to save the converted percussion MIDI file.
  """
  print(f"Reading MIDI file: {input_file}")  # Added print statement
  midi_file = mido.MidiFile(input_file)
  
  # Create a new MIDI track to store percussion instruments
  percussion_track = mido.MidiTrack()
  midi_file.tracks.append(percussion_track)

  for track in midi_file.tracks:
    for msg in track:
      print(f"Processing message: {msg}")  # Added print statement
      if msg.type == 'program_change' and msg.channel == 9:  # Check channel and type
        # Skip program change message (optional)
        pass
      elif msg.type == 'note_on':
        new_msg = mido.Message(msg.type, note=msg.note, velocity=msg.velocity, time=msg.time, channel=9)
        percussion_track.append(new_msg)
        continue
      

      # elif msg.type == 'note_off' and msg.track != percussion_track:  # Check message origin (optional)
      #   print(f"Processing note_off message: {msg}")  # Added print statement
      #   # Create a corresponding note_off message for percussion track
      #   new_msg_off = mido.Message('note_off', note=msg.note, velocity=msg.velocity, time=msg.time, channel=9)
      #   percussion_track.append(new_msg_off)
      # break
      
  # Check percussion track content after processing
  print(f"Number of messages in percussion track: {len(percussion_track)}")

  # Save the converted MIDI file
  try:
      print(f"Saving converted MIDI file to: {output_file}")
      midi_file.save(output_file)
  except Exception as e:
      print(f"Error saving converted MIDI file: {e}")

# Example usage
input_file = "breakthebrake.mid"
output_file = "percussion.mid"
convert_to_percussion_midi(input_file, output_file)
print(f"Converted MIDI file saved to: {output_file}")
