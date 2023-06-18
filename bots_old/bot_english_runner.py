#!/usr/bin/env python3

import os
import time

from config import create_api
from modules.tweet import tweet
from modules.get_date import get_date

api = create_api()

maxtries = 8    # 8 * 15 minutes = about 2 hours total of waiting,
home = os.getenv("HOME")
project_path = '/%s/estudio/tweepy_bot' % (home)
data = '/%s/scrapers/today_in_history.txt' % (project_path)

source = "[©2023 Encyclopædia Britannica, Inc.]"
tag = "🤖 #TodayInHistory"

date = get_date(format="eng")

for i in range(maxtries):
    try:
        tweet(api, tag, date, data, source)
        break
    except Exception as i:
        time.sleep(900)
        print("fail", i)
