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
    if cleaner is True:
        with open(data, 'r') as filename:
            lines = filename.readlines()

        # Find the longest line
        # myline = max(lines, key=len)
        myline = random.choice(lines)

        lines.pop(lines.index(myline))

        with open(data, 'w') as filename:
            filename.writelines(lines)

        mystr = myline.strip()

    else:
        with open(data, 'r') as filename:
            lines = filename.readlines()

        # Find the longest line
        # myline = max(lines, key=len)
        myline = random.choice(lines)

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


def split_string(string):
    """Function to split string according to tweeter word boundaries.

    Args:
        string (str): string to be splitted.

    Returns:
        List of strings
    """
    if len(string) > 234:
        # First 234 characters
        first_string = string[:234]
        # Find the last space within the first 234 characters
        last_space_index = first_string.rfind(' ')
        if last_space_index != -1:
            # Truncate to the last space
            first_string = first_string[:last_space_index]
        # Remaining characters after first_string
        remaining_string = string[len(first_string):].strip()
        if len(remaining_string) > 234:
            # First 240 characters from remaining_string
            second_string = remaining_string[:234]
            # Find the last space within the first 240 characters
            last_space_index = second_string.rfind(' ')
            if last_space_index != -1:
                # Truncate to the last space
                second_string = second_string[:last_space_index]
            # Remaining characters after second_string
            third_string = remaining_string[len(second_string):].strip()
        else:
            second_string = remaining_string
            third_string = ""
    else:
        first_string = string
        second_string = ""
        third_string = ""

    return first_string, second_string, third_string


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
