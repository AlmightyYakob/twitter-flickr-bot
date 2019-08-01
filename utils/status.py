import json


def createStatusFromPhoto(photo):
    print(json.dumps(photo, indent=4))
    url = photo["urls"]["url"][0]["_content"]
    hashtags = list(map(lambda x: f"#{x['_content']}", photo["tags"]["tag"]))
    title = photo["title"]["_content"]
    description = photo["description"]["_content"]

    if not title[0].isupper():
        title = title.capitalize()

    return f"{title}\n{description}\n{' '.join(hashtags)}\n{url}"
