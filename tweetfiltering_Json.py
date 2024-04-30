import json
import csv

import pandas as pd
tweets = []

# Open the tweets.json file and load its contents line by line
with open('tweets.json', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        try:
            tweet_data = json.loads(line)
            if isinstance(tweet_data, dict):
                tweet_text = tweet_data.get('tweet', {}).get('full_text', '')  # Safely get tweet text
                if tweet_text:
                    tweets.append(tweet_text)

        except json.JSONDecodeError as e:
            print(f"Ignoring line: {line.strip()}")

# Print the text of each tweet
for tweet in tweets:
    print(tweet)


# filtered_tweets = [tweet for tweet in tweets if 'entities' in tweet['tweet'] and 'hashtags' in tweet['tweet']['entities'] and any(tag['text'] == '챌린지_매일슬덩그리기' for tag in tweet['tweet']['entities']['hashtags'])]

#   # Print the filtered tweets in a readable format
# for tweet in filtered_tweets:
#   print(json.dumps(tweet, indent=4, ensure_ascii=False))


  # first_tweet_text = tweets[0]['tweet']['full_text']
  # first_tweet_id = tweets[0]['tweet']['id_str']

  # # Loop through all tweets
  # for tweet in tweets:
  #   print(f"Tweet text: {tweet['tweet']['full_text']}")
  #   print(f"Tweet ID: {tweet['tweet']['id_str']}")

# except json.JSONDecodeError as e:
#   print("Error parsing JSON data:", e)
# except IOError as e:
#   print(e)