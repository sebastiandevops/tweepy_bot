#!/usr/bin/python3
import tweepy
import random

from datetime import datetime
from utils.split_string import split_string
# Authenticate to Twitter


def tweet_job():
    auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
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
    with open('/home/sebastian/estudio/tweepy_bot/today_in_history.txt','r') as filename:
        lines = filename.readlines()

    myline = random.choice(lines)

    deleted_line = lines.pop(lines.index(myline))

    with open('/home/sebastian/estudio/tweepy_bot/today_in_history.txt','w') as filename:
        filename.writelines(lines)

    # Get the current date
    current_date = datetime.now()

    # Format the date as "month day"
    formatted_date = current_date.strftime("%B %d")
    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    myline = myline
    mystr = myline.strip()
    mystr = f"🤖 #OnThisDay, {formatted_date}, " + mystr

    firstStr, secondStr = split_string(mystr)
    if secondStr == "":
        original_tweet = api.update_status(status=mystr)
        print(mystr)
    else:
        firstStr = firstStr + " [1/2]"
        secondStr = secondStr + " [2/2]"
        original_tweet = api.update_status(status=firstStr)
        reply1_tweet = api.update_status(status=secondStr,
                                         in_reply_to_status_id=original_tweet.id,
                                         auto_populate_reply_metadata=True)
        print(f"First tweet: {firstStr}\n second tweet: {secondStr}")
    api.update_status(status=mystr)
    print(mystr)
