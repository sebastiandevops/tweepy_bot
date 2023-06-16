#!/usr/bin/python3
import random

from bots.config import create_api
import os

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal

from utils.split_string import split_string
# Authenticate to Twitter


def tweet_job(api):
    home = os.getenv("HOME")
    data = '/%s/estudio/tweepy_bot/scrapers/hoy_en_la_historia.txt' % (home)
    with open(data, 'r') as filename:
        lines = filename.readlines()

    # Find the longest line
    # myline = max(lines, key=len)
    myline = random.choice(lines)

    lines.pop(lines.index(myline))

    with open(data, 'w') as filename:
        filename.writelines(lines)

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
    mystr = f"🤖 #HoyEnLaHistoria, {formatted_date}, " + mystr + " [© 2012-2023 Hoyenlahistoria.com]"

    if len(mystr) <= 240:
        response = api.create_tweet(text=mystr)
        print(mystr)
    else:
        firstStr, secondStr, thirdStr = split_string(mystr)
        if thirdStr == "":
            firstStr = firstStr + " [1/2]"
            secondStr = secondStr + " [2/2]"
            response = api.create_tweet(text=firstStr)
            print(response.data['id'])
            api.create_tweet(text=secondStr,
                             in_reply_to_tweet_id=response.data['id']
                             )
            print(f"First tweet: {firstStr}\nsecond tweet: {secondStr}")
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


def main():
    api = create_api()
    tweet_job(api)


if __name__ == "__main__":
    main()
