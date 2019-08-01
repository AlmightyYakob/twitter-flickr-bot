from flickr.interaction import getNextPhoto
from twitter.interaction import postTweet, reverseGeocode
from utils.status import createStatusFromPhoto


def main():
    photo = getNextPhoto()

    placeId = None
    if "location" in photo:
        placeId = reverseGeocode(
            photo["location"]["latitude"],
            photo["location"]["longitude"],
            photo["location"]["accuracy"],
        )

    status = createStatusFromPhoto(photo)
    postTweet(status, meta={"place_id": placeId})


if __name__ == "__main__":
    main()
