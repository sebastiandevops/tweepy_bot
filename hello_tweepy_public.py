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
    # open Robin's Edgar Allen Poe data file and read every line into memory
    with open('/home/sebastian/Holberton/tweepy_bot/history.txt','r') as filename:
        lines = filename.readlines()
    myline =random.choice(lines)

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    myline = myline + '#thingsthathappened'
    mystr = myline.replace("\n"," ")
    api.update_status(status=mystr)
    print(mystr)

tweet_job()
