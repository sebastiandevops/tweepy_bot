#!/usr/bin/env python3

import os

from bots.bots import tweet_end
import time

maxtries = 8    # 8 * 15 minutes = about 2 hours total of waiting,
home = os.getenv("HOME")
project_path = '/%s/estudio/tweepy_bot' % (home)
data = '/%s/hoy_en_la_historia.txt' % (project_path)

source = {
    "esp": "[© 2012-2023 Hoyenlahistoria.com]",
    "en":  "[©2023 Encyclopædia Britannica, Inc.]"
}

for i in range(maxtries):
    try:
        tweet_end(data, source["esp"])
        break
    except:
        time.sleep(900)
        print("fail", i)
