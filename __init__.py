from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv
import os

from flickr.interaction import getNextPhoto
from twitter.interaction import postTweet
from utils.status import createStatusFromPhoto

load_dotenv()
CRON_TIME_HOUR = os.getenv("CRON_TIME_HOUR")
CRON_TIME_MINUTE = os.getenv("CRON_TIME_MINUTE")
CRON_TIME_SECOND = os.getenv("CRON_TIME_SECOND")
TIME_INTERVAL_SECONDS = os.getenv("TIME_INTERVAL")


def main():
    photo = getNextPhoto()

    if photo:
        status = createStatusFromPhoto(photo)
        postTweet(status)


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    if CRON_TIME_HOUR and CRON_TIME_MINUTE and CRON_TIME_SECOND:
        scheduler.add_job(
            main,
            "cron",
            hour=CRON_TIME_HOUR,
            minute=CRON_TIME_MINUTE,
            second=CRON_TIME_SECOND,
        )
    elif TIME_INTERVAL_SECONDS:
        scheduler.add_job(main, "interval", seconds=TIME_INTERVAL_SECONDS)
    else:
        raise Exception(
            "No scheduler time specified. Have you configured your .env file?"
        )
    scheduler.start()
