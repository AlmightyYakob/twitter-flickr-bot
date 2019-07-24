from flickr.interaction import getRandomPhoto
from twitter.interaction import postTweet
from utils.status import createStatusFromPhoto

photo = getRandomPhoto()
status = createStatusFromPhoto(photo)
postTweet(status)
