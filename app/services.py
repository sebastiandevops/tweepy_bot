#!/usr/bin/env python3

import random

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal


def get_line(hashtag, date_format, data, source, cleaner):
    """
    Retrieve a line to be tweeted based on the provided parameters.

    Args:
        hashtag (str): The hashtag for the tweet.
        date_format (str): Should be "eng" or "esp".
        data (str): The path to the data file to be read.
        source (str): The data source.
        cleaner (bool): Indicates whether to clean the source file.

    Returns:
        str: The line to be tweeted.
    """
    try:
        text = read_file(data, cleaner)
        if date_format is None:
            text = f'{hashtag}: {text} {source}'
        else:
            text = f'{hashtag}, {date_format}, {text} {source}'
        return text
    except FileNotFoundError as e:
        print(f"Error: File '{data}' not found. {str(e)}")
    except Exception as e:
        print(f"An error occurred while retrieving the tweet line: {str(e)}")
    return None


def read_file(data, cleaner):
    """
    Read the file and optionally clean the line if cleaner is True.

    Args:
        data (str): The data to read from the file.
        cleaner (bool): Indicates whether to clean the source file.

    Returns:
        str: The text to populate the tweet.
    """
    with open(data, 'r') as filename:
        lines = filename.readlines()

    myline = random.choice(lines)

    if cleaner:
        lines.remove(myline)
        with open(data, 'w') as filename:
            filename.writelines(lines)

    text = myline.strip()
    return text


def create_tweet(api, text):
    """
    Create a single tweet or thread using the Twitter API.

    Args:
        api: The Twitter API object.
        text (str): The string to be processed.
    """
    try:
        if len(text) <= 240:
            response = api.create_tweet(text=text)
            responseStr = "************ Response Object ************\
                           \n{}".format(response)
            print(responseStr.lstrip())
        else:
            tweets = split_string(text)
            n_tweets = len(tweets)
            logs = []
            if n_tweets > 1:
                firstStr = tweets[0] + " [1/%s]" % (str(n_tweets))
                response = api.create_tweet(text=firstStr)
                i = 2
                for tweet in tweets[1:]:
                    otherStr = tweet + " [%s/%s]" % (str(i), str(n_tweets))
                    logs.append(response)
                    response = api.create_tweet(
                        text=otherStr,
                        in_reply_to_tweet_id=response.data['id']
                    )
                    i += 1
                logs.append(response)
            for i, item in enumerate(logs, start=1):
                logsStr = "************ Response Object ************\
                           \nResponse {}: {}\n".format(i, item)
                print(logsStr.lstrip())
        print("Tweeted successfully!")
    except Exception as e:
        print(f"An error occurred while creating the tweet: {str(e)}")


def split_string(string):
    """
    Split the string into segments based on Twitter's character limit.

    Args:
        string (str): The string to be split.

    Returns:
        list: List of strings representing the segmented tweets.
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


def get_date(date_format=""):
    """
    Create a formatted date.

    Args:
        date_format (str): The format for the date (either "esp" or "eng").

    Returns:
        str: The formatted date.
    """
    try:
        if date_format == "esp":
            # Get the current date
            current_date = datetime.now()

            # Format the date components separately
            day = format_decimal(current_date.day, format='##')
            month = format_date(current_date, format='MMMM', locale='es')

            # Format the date as "month day"
            # Create the formatted date with "de" separator
            formatted_date = f"{day} de {month}"

        elif date_format == "eng":
            # Get the current date
            current_date = datetime.now()

            # Format the date as "month day"
            formatted_date = current_date.strftime("%B %d")
        else:
            raise ValueError("Invalid date format")
    except ValueError as e:
        print(f"Error {e}")
        return None

    return formatted_date
