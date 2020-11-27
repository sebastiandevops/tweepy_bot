#!/usr/bin/python3
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler
import random
# Authenticate to Twitter

def tweet_job():
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

    # Create API object
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    # Create a tweet
    # open data file and read every line into memory
    with open('/path/to/file.txt','r') as filename:
        lines = filename.readlines()
    #select random line from lines
    myline =random.choice(lines)

    # Tweet my line
    # Yoy have to add this script to crontab -e to automatically runs.
    # For example, if you add this line to crontab
    # 0 9 * * * /full/path/to/script/hello_tweepy.py
    # The script will execute every day at 9am.
    myline = myline + '#thingsthathappened'
    mystr = myline.replace("\n"," ")
    api.update_status(status=mystr)
    print(mystr)

tweet_job()
