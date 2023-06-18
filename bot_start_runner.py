#!/usr/bin/env python3

import os
import time

from bots.config import create_api
from bots.bots import tweet_start
from utils.get_date import get_date_spanish

api = create_api()

maxtries = 8    # 8 * 15 minutes = about 2 hours total of waiting,
home = os.getenv("HOME")
project_path = '/%s/estudio/tweepy_bot' % (home)
data = '/%s/scrapers/hoy_en_la_historia.txt' % (project_path)

source = "[© 2012-2023 Hoyenlahistoria.com]"

date = get_date_spanish()

for i in range(maxtries):
    try:
        tweet_start(api, date, data, source)
        break
    except:
        time.sleep(900)
        print("fail", i)
