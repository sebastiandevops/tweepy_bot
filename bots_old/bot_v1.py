#!/usr/bin/python3
from bots.config import create_api

import random
from utils.split_string import split_string
# Authenticate to Twitter


def tweet_job(api):
    data = '/home/sebastian/projects/tweepy_bot/scrapers/history.txt'
    with open(data, 'r') as filename:
        lines = filename.readlines()

    myline = random.choice(lines)

    lines.pop(lines.index(myline))

    with open(data, 'w') as filename:
        filename.writelines(lines)

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    myline = myline
    mystr = myline.strip()
    mystr = "🤖 #History " + mystr

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
