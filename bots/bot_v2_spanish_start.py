#!/usr/bin/python3
import random

from bots.config import create_api

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal

from utils.split_string import split_string
# Authenticate to Twitter


def tweet_job(api):
    data = '/home/sebastian/estudio/tweepy_bot/scrapers/hoy_en_la_historia.txt'
    with open(data, 'r') as filename:
        lines = filename.readlines()

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
    mystr = f"🤖 #HoyEnLaHistoria, {formatted_date}, " + mystr
    + " [© 2012-2023 Hoyenlahistoria.com]"

    if len(mystr) <= 240:
        original_tweet = api.update_status(status=mystr)
        print(mystr)
    else:
        firstStr, secondStr = split_string(mystr)
        firstStr = firstStr + " [1/2]"
        secondStr = secondStr + " [2/2]"
        original_tweet = api.update_status(status=firstStr)
        api.update_status(status=secondStr,
                          in_reply_to_status_id=original_tweet.id,
                          auto_populate_reply_metadata=True)
        print(f"First tweet: {firstStr}\nsecond tweet: {secondStr}")


def main():
    api = create_api()
    tweet_job(api)


if __name__ == "__main__":
    main()
