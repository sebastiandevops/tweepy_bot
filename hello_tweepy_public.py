#!/usr/bin/python3
import tweepy

import random
# Authenticate to Twitter


def tweet_job():
    auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

    # Create API object
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except SystemExit:
        print("Error during authentication")
        raise
    # Create a tweet
    # open Robin's Edgar Allen Poe data file and read every line into memory
    with open('/home/sebastian/estudio/tweepy_bot/history.txt', 'r') as filename:
        lines = filename.readlines()

    myline = random.choice(lines)

    lines.pop(lines.index(myline))

    with open('/home/sebastian/estudio/tweepy_bot/history.txt', 'w') as filename:
        filename.writelines(lines)

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    #myline = myline
    mystr = myline.replace("\n", " ")
    api.update_status(status=mystr)
    print(mystr)

