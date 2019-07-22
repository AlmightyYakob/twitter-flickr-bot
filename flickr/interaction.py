import json
import os
import flickrapi

flickrDir = os.path.dirname(os.path.abspath(__file__))
with open(f'{flickrDir}/credentials.json') as credentialsFile:
  credentials = json.load(credentialsFile)

flickr = flickrapi.FlickrAPI(credentials['API_KEY'], credentials['API_SECRET'], format='json')
photoInfo = json.loads(flickr.people.getPhotos(user_id=credentials['USERNAME']))
photos = photoInfo['photos']['photo']
# print(json.dumps(photos, indent=4))

for photo in photos:
  photoSizes = json.loads(flickr.photos.getSizes(photo_id=photo['id']))['sizes']
  # print(json.dumps(photoSizes, indent=4))
  photoLinks = [x['source'] for x in photoSizes['size'] if x['label'] == 'Original']
  print(json.dumps(photoLinks, indent=4))
