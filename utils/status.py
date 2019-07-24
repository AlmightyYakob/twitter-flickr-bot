import json

def createStatusFromPhoto(photo):
  photo = photo['photo']
  url = photo['urls']['url'][0]['_content']
  hashtags = list(map(lambda x: f"#{x['_content']}", photo['tags']['tag']))
  title = photo['title']['_content']

  if (not title[0].isupper()):
    title = title.capitalize()

  return f"{title}\n{' '.join(hashtags)}\n{url}"
