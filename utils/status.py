import json

def createStatusFromPhoto(photo):
  print(json.dumps(photo, indent=4))
  photo = photo['photo']
  url = photo['urls']['url'][0]['_content']
  hashtags = list(map(lambda x: f"#{x['_content']}", photo['tags']['tag']))
  title = photo['title']['_content']

  return f"{title}\n{' '.join(hashtags)}\n{url}"
