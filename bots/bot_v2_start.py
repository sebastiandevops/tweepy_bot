#!/usr/bin/python3
import random
from bots.config import create_api

from datetime import datetime
from utils.split_string import split_string
# Authenticate to Twitter


def tweet_job(api):
    data = '/home/sebastian/estudio/tweepy_bot/scrapers/today_in_history.txt'
    with open(data, 'r') as filename:
        lines = filename.readlines()

    myline = random.choice(lines)

    lines.pop(lines.index(myline))

    with open(data, 'w') as filename:
        filename.writelines(lines)

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
        original_tweet = api.update_status(status=mystr)
        print(mystr)
    else:
        firstStr, secondStr, thirdStr = split_string(mystr)
        if thirdStr == "":
            firstStr = firstStr + " [1/2]"
            secondStr = secondStr + " [2/2]"
            original_tweet = api.update_status(status=firstStr)
            api.update_status(status=secondStr,
                              in_reply_to_status_id=original_tweet.id,
                              auto_populate_reply_metadata=True)
            print(f"First tweet: {firstStr}\nsecond tweet: {secondStr}")
        else:
            firstStr = firstStr + " [1/2]"
            secondStr = secondStr + " [2/3]"
            thirdStr = thirdStr + " [3/3]"
            original_tweet = api.update_status(status=firstStr)
            reply1 = api.update_status(
                status=secondStr,
                in_reply_to_status_id=original_tweet.id,
                auto_populate_reply_metadata=True)
            api.update_status(
                status=thirdStr,
                in_reply_to_status_id=reply1.id,
                auto_populate_reply_metadata=True)
            print(f"First tweet: {firstStr}\nsecond tweet: {secondStr}\nthird tweet: {thirdStr}")


def main():
    api = create_api()
    tweet_job(api)


if __name__ == "__main__":
    main()
