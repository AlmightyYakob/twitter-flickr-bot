import json
import os
from random import randint

import flickrapi

flickrDir = os.path.dirname(os.path.abspath(__file__))
with open(f'{flickrDir}/credentials.json') as credentialsFile:
  credentials = json.load(credentialsFile)
flickr = flickrapi.FlickrAPI(credentials['API_KEY'], credentials['API_SECRET'], format='json')

def getRandomPhoto():
  photoInfo = json.loads(flickr.people.getPhotos(user_id=credentials['USERNAME']))
  photos = photoInfo['photos']['photo']

  photo = photos[randint(0, len(photos) - 1)]
  # photoSizes = json.loads(flickr.photos.getSizes(photo_id=photo['id']))['sizes']
  # photoLink = [x['source'] for x in photoSizes['size'] if x['label'] == 'Original'][0]

  url = json.loads(flickr.photos.getInfo(photo_id=photo['id']))['photo']['urls']['url'][0]['_content']
  return url
