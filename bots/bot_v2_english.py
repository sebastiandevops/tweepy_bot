#!/usr/bin/python3
from bots.config import create_api
import random
import os

from datetime import datetime

from utils.split_string import split_string
# Authenticate to Twitter


def tweet_job(api):
    home = os.getenv("HOME")
    data = '/%s/estudio/tweepy_bot/scrapers/today_in_history.txt' % (home)
    with open(data, 'r') as filename:
        lines = filename.readlines()

    myline = random.choice(lines)

    # Get the current date
    current_date = datetime.now()

    # Format the date as "month day"
    formatted_date = current_date.strftime("%B %d")

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    myline = myline
    mystr = myline.strip()
    mystr = f"🤖 #OnThisDay, {formatted_date}, " + mystr + " [©2023 Encyclopædia Britannica, Inc.]"

    if len(mystr) <= 240:
        response = api.create_tweet(text=mystr)
        print(f"Tweet: {mystr}")
        print(response)
    else:
        firstStr, secondStr, thirdStr = split_string(mystr)
        if thirdStr == "":
            firstStr = firstStr + " [1/2]"
            secondStr = secondStr + " [2/2]"
            response = api.create_tweet(text=firstStr)
            api.create_tweet(
                text=secondStr,
                in_reply_to_tweet_id=response.data['id']
            )
            print(f"First tweet: {firstStr}\nsecond tweet: {secondStr}")
            print(response)
        else:
            firstStr = firstStr + " [1/3]"
            secondStr = secondStr + " [2/3]"
            thirdStr = thirdStr + " [3/3]"
            response = api.create_tweet(text=firstStr)
            reply1 = api.create_tweet(
                status=secondStr,
                in_reply_to_tweet_id=response.data['id']
            )
            api.create_tweet(
                status=thirdStr,
                in_reply_to_tweet_id=reply1.data['id']
            )
            print(f"First tweet: {firstStr}\n"
                  f"second tweet: {secondStr}\n"
                  f"third tweet: {thirdStr}")
            print(response)


def main():
    api = create_api()
    tweet_job(api)


if __name__ == "__main__":
    main()
