#!/usr/bin/env python3
from bots.bots import tweet_start
import time

maxtries = 8    # 8 * 15 minutes = about 2 hours total of waiting,

for i in range(maxtries):
    try:
        tweet_start()
        break
    except:
        time.sleep(900)
        print("fail", i)
