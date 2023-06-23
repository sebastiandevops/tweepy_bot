#!/usr/bin/env python3

import os
import time

from app.models import TweepyBot
# from app.services import get_date


if __name__ == '__main__':

    maxtries = 8    # 8 * 15 minutes = about 2 hours total of waiting,
    home = os.getenv("HOME")
    project_path = '%s/estudio/tweepy_bot' % (home)
    data = '%s/scrapers/history.txt' % (project_path)

    hashtag = "🤖 #Historia"

    for i in range(maxtries):
        try:
            bot = TweepyBot(
                text="This is a test",
            )
            tweet_content = bot.prepare_tweet()
            bot.post_tweet(tweet_content)
            print(bot.__str__())
            break
        except Exception as i:
            time.sleep(900)
            print("fail", i)
