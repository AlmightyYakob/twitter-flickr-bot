import os
import tweepy
from dotenv import load_dotenv

load_dotenv()


def authenticate():
    auth = tweepy.OAuthHandler(
        os.getenv("TWITTER_CONSUMER_API_KEY"), os.getenv("TWITTER_CONSUMER_API_SECRET")
    )
    auth.set_access_token(
        os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )
    return tweepy.API(auth)


def reverseGeocode(lat, lng, accuracy):
    api = authenticate()
    place = api.reverse_geocode(lat=lat, long=lng, accuracy=accuracy)[0]
    return place.id


def postTweet(status, meta={}):
    api = authenticate()
    api.update_status(status, place_id=meta["place_id"])
