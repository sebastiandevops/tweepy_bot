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
data = '/%s/scrapers/hoy_en_la_historia.txt' % (project_path)

source = "[© 2012-2023 Hoyenlahistoria.com]"
tag = "🤖 #HoyEnLaHistoria"
date = get_date(format="esp")

for i in range(maxtries):
    try:
        tweet(api, tag, date, data, source, cleaner=True)
        break
    except Exception as i:
        time.sleep(900)
        print("fail", i)
