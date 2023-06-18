#!/usr/bin/env python3

import random

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal


def get_line(tag, date, data, source, cleaner):

    """Function to read data and get the line to be tweeted

    Args:
        tag (str): Hashtag for the tweet.
        date (str): Should be "eng" or "esp".
        data (str): Data file path to be readed.
        cleaner (boolean): It tells the function
                           if data should be cleaned.
        source (str): Data source.

    Returns:
        mystr (str): line for the tweet.
    """
    mystr = read_file(data, cleaner)

    mystr = f'{tag}, {date}, {mystr} {source}'

    return mystr


def read_file(data, cleaner):

    """Function to read file and clean the line it cleaner is True

    Args:
        data (str): Data to read from file
        cleaner (boolean): It tells the function if should
                           clean the source file.

    Returns:
        mystr (str): the text to pupulaate the tweet
    """
    with open(data, 'r') as filename:
        lines = filename.readlines()

    myline = random.choice(lines)

    if cleaner:
        lines.remove(myline)
        with open(data, 'w') as filename:
            filename.writelines(lines)

    mystr = myline.strip()
    return mystr


def create_tweet(api, mystr):

    """Function to create a sigle tweet or thread

    Args:
        api (str): Twitter API object
        mystr (str): String to be processed
    """

    if len(mystr) <= 240:
        response = api.create_tweet(text=mystr)
        print(f"Tweet: {mystr}")
    else:
        tweets = split_string(mystr)
        n_tweets = len(tweets)
        if n_tweets > 1:
            firstStr = tweets[0] + " [1/%s]" % (str(n_tweets))
            response = api.create_tweet(text=firstStr)
            i = 2
            for tweet in tweets[1:]:
                otherStr = tweet + " [%s/%s]" % (str(i), str(n_tweets))
                response = api.create_tweet(
                    text=otherStr,
                    in_reply_to_tweet_id=response.data['id']
                )
                i += 1
    print("Tweeted successfully!")


def split_string(string):
    """Function to split string according to tweeter word boundaries.

    Args:
        string (str): string to be splitted.

    Returns:
        List of strings
    """
    tweets = []

    if len(string) <= 234:
        tweets.append(string)
    else:
        remaining_string = string
        while len(remaining_string) > 234:
            # First 240 characters from remaining_string
            new_string = remaining_string[:234]
            # Find the last space within the first 240 characters
            last_space_index = new_string.rfind(' ')
            if last_space_index != -1:
                # Truncate to the last space
                new_string = new_string[:last_space_index]
            tweets.append(new_string)
            # Remaining characters after second_string
            remaining_string = remaining_string[len(new_string):].strip()

        if len(remaining_string) > 0:
            tweets.append(remaining_string)

    return tweets


def get_date(format=""):
    """Function to create a formatted date

    Args:
        format (str): esp or eng format

    Returns:
        formatted_date (str)
    """
    try:
        if format == "esp":
            # Get the current date
            current_date = datetime.now()

            # Format the date components separately
            day = format_decimal(current_date.day, format='##')
            month = format_date(current_date, format='MMMM', locale='es')

            # Format the date as "month day"
            # Create the formatted date with "de" separator
            formatted_date = f"{day} de {month}"

        elif format == "eng":
            # Get the current date
            current_date = datetime.now()

            # Format the date as "month day"
            formatted_date = current_date.strftime("%B %d")
    except Exception as e:
        e = "format parameter should be [esp] or [eng]"
        print(e)

    return formatted_date
