"""
@Jordan Taylor
Simple python script to run and determine emotional/subjectivity context from Tweets
"""
import csv
import tweepy
import numpy as np
from textblob import TextBlob

# credentials
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Mondays')
total_tweets = len(public_tweets)

sentiment = np.chararray((1, total_tweets), itemsize=15)
emotion = np.empty([1, total_tweets])
subjective = np.empty([1, total_tweets])

for i in range(total_tweets):
    analysis = TextBlob(public_tweets[i].text)
    emotion[0, i] = analysis.sentiment.polarity
    subjective[0, i] = analysis.sentiment.subjectivity
    if emotion [0, i] < 0:
        sentiment[0, i] = 'Negative'
    elif emotion [0, i] == 0:
        sentiment[0, i] = 'None'
    else:
        sentiment[0, i] = 'Positive'


with open('sentiment_analysis.csv', 'w') as csvfile:
    fieldnames = ['Tweet', 'Sentiment', 'Emotion', 'Subjectivity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(total_tweets):
        writer.writerow({
            'Tweet':(public_tweets[i].text).encode('utf-8'),
            'Sentiment': str(sentiment[0, i]),
            'Emotion': str(emotion[0, i])
            'Subjectivity': str(subjective[0, i])
        })
