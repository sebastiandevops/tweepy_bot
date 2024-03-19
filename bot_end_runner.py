#!/usr/bin/env python3

import os
import time

from app.models import TweepyBot


if __name__ == '__main__':

    maxtries = 8    # 8 * 15 minutes = about 2 hours total of waiting,
    home = os.getenv("HOME")
    project_path = '%s/projects/tweepy_bot' % (home)
    data_file = '%s/scrapers/hoy_en_la_historia.txt' % (project_path)

    for i in range(maxtries):
        try:
            bot = TweepyBot(
                hashtag="🤖 #HoyEnLaHistoria",
                date_format="esp",
                data=data_file,
                source="[©2012-2023 Hoyenlahistoria.com]"
            )
            tweet_content = bot.prepare_tweet()
            bot.post_tweet(tweet_content)
            print(bot.__str__())
            break
        except Exception as i:
            time.sleep(900)
            print("fail", i)
