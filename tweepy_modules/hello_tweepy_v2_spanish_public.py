#!/usr/bin/python3
import tweepy
import random

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal

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
    with open('/home/sebastian/estudio/tweepy_bot/hoy_en_la_historia.txt', 'r') as filename:
        lines = filename.readlines()

    myline = random.choice(lines)

    deleted_line = lines.pop(lines.index(myline))

    # with open('/home/sebastian/estudio/tweepy_bot/history.txt','w') as filename:
        # filename.writelines(lines)

    # Set the locale to Spanish
    # locale.setlocale(locale.LC_ALL, 'es_ES')

    # Get the current date
    current_date = datetime.now()

    # Format the date components separately
    day = format_decimal(current_date.day, format='##')
    month = format_date(current_date, format='MMMM', locale='es')

    # Format the date as "month day"
    # Create the formatted date with "de" separator
    formatted_date = f"{day} de {month}"

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    myline = myline
    mystr = myline.strip()
    mystr = f"🤖 #HoyEnLaHistoria, {formatted_date}, " + mystr

    if len(mystr) <= 240:
        original_tweet = api.update_status(status=mystr)
        print(mystr)
    else:
        firstStr, secondStr = split_string(mystr)
        firstStr = firstStr + " [1/2]"
        secondStr = secondStr + " [2/2]"
        original_tweet = api.update_status(status=firstStr)
        reply1_tweet = api.update_status(status=secondStr,
                                         in_reply_to_status_id=original_tweet.id,
                                         auto_populate_reply_metadata=True)
        print(f"First tweet: {firstStr}\nsecond tweet: {secondStr}")
