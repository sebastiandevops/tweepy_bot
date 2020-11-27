#!/usr/bin/python3
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler
import random
# Authenticate to Twitter

def tweet_job():
    auth = tweepy.OAuthHandler("tW6qoWBTGF4hyWs6Rt6g3pzzU", "xNK1ofrJtoKMCwHyUIMbYXy3bBoXD0BP1dwbjFMpFtyf3SnL7u")
    auth.set_access_token("1226500246970261504-kaPjqgk9qc224YwmMDqN0mdcbnR0Pv", "B19Xy5ACm0J8q9HFVyKpqKR4fbCUEmOArceKp0VclIs55")

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
