import os
import json
import tweepy

twitterDir = os.path.dirname(os.path.abspath(__file__))
with open(f'{twitterDir}/credentials.json') as credentialsFile:
  credentials = json.load(credentialsFile)


def authenticate():
  auth = tweepy.OAuthHandler(credentials['CONSUMER_API_KEY'], credentials['CONSUMER_API_SECRET'])
  auth.set_access_token(credentials['ACCESS_TOKEN'], credentials['ACCESS_TOKEN_SECRET'])
  return tweepy.API(auth)


def postTweet(status):
  api = authenticate()
  api.update_status(status)
