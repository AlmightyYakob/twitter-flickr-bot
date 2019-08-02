import json
import os
from random import randint
from dotenv import load_dotenv
import flickrapi
from sqlitedict import SqliteDict

LAST_FLICKR_TIMESTAMP = "last_flickr_timestamp"

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
FLICKR_API_KEY = os.getenv("FLICKR_API_KEY")
FLICKR_API_SECRET = os.getenv("FLICKR_API_SECRET")
FLICKR_USERNAME = os.getenv("FLICKR_USERNAME")

db = SqliteDict(DB_NAME, autocommit=True)
flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET, format="json")

if LAST_FLICKR_TIMESTAMP not in db:
    BEGINNING_TIMESTAMP = os.getenv("BEGINNING_TIMESTAMP")
    db[LAST_FLICKR_TIMESTAMP] = BEGINNING_TIMESTAMP


def addPhotoGeo(photo):
    if "location" in photo:
        return

    geo = json.loads(flickr.photos.geo.getLocation(photo_id=photo["id"]))

    if geo["stat"] != "ok":
        return
    else:
        geo = geo["photo"]

    newPhoto = dict(photo)
    newPhoto["location"] = geo["location"]
    return newPhoto


def getSpecificPhoto(photo_id):
    photo = json.loads(flickr.photos.getInfo(photo_id=photo_id))
    return photo


def getRandomPhoto():
    photoInfo = json.loads(flickr.people.getPhotos(user_id=FLICKR_USERNAME))
    photos = photoInfo["photos"]["photo"]
    photo = photos[randint(0, len(photos) - 1)]

    return json.loads(flickr.photos.getInfo(photo_id=photo["id"]))["photo"]


def getNextPhoto():
    lastPhotoTimestamp = db[LAST_FLICKR_TIMESTAMP]
    photoInfo = json.loads(
        flickr.people.getPhotos(
            user_id=FLICKR_USERNAME, min_upload_date=int(lastPhotoTimestamp) + 1
        )
    )
    photos = photoInfo["photos"]["photo"]

    if len(photos) > 1:
        photo = photos[-1]
    elif len(photos) == 1:
        photo = photos[0]
    else:
        print("No new photos found, skipping...")
        return None

    photo = json.loads(flickr.photos.getInfo(photo_id=photo["id"]))["photo"]
    db[LAST_FLICKR_TIMESTAMP] = int(photo["dates"]["posted"])

    return photo
