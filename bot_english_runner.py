#!/usr/bin/env python3

import os
import time

from app.models import TweepyBot
from app.services import get_date


if __name__ == '__main__':

    maxtries = 8    # 8 * 15 minutes = about 2 hours total of waiting,
    home = os.getenv("HOME")
    project_path = '%s/estudio/tweepy_bot' % (home)
    data = '%s/scrapers/today_in_history.txt' % (project_path)
    date = get_date(date_format="eng")

    for i in range(maxtries):
        try:
            app = TweepyBot(
                hashtag="🤖 #OnThisDay",
                date=date,
                data=data,
                source="[©2023 Encyclopædia Britannica, Inc.]"
            )
            mystr = app.prepare_tweet()
            app.post_tweet(mystr)
            print(app.__str__())
            break
        except Exception as i:
            time.sleep(900)
            print("fail", i)
