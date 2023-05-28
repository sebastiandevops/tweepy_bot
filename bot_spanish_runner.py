#!/usr/bin/env python3
from tweepy_modules.hello_tweepy_v2_spanish import tweet_job
import time

maxtries = 8    # 8 * 15 minutes = about 2 hours total of waiting,

for i in range(maxtries):
    try:
        tweet_job()
        break
    except:
        time.sleep(900)
        print("fail", i)
