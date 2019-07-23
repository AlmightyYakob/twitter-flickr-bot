import json
import os
from random import randint
from dotenv import load_dotenv
import flickrapi

load_dotenv()
flickr = flickrapi.FlickrAPI(os.getenv('FLICKR_API_KEY'), os.getenv('FLICKR_API_SECRET'), format='json')


def getRandomPhoto():
  photoInfo = json.loads(flickr.people.getPhotos(user_id=os.getenv('FLICKR_USERNAME')))
  photos = photoInfo['photos']['photo']
  photo = photos[randint(0, len(photos) - 1)]

  url = json.loads(flickr.photos.getInfo(photo_id=photo['id']))['photo']['urls']['url'][0]['_content']
  return url
