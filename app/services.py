#!/usr/bin/env python3

import random

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal


def get_line(hashtag, formatted_date, data, source, cleaner):
    """
    Retrieve a line to be tweeted based on the provided parameters.

    Args:
        hashtag (str): The hashtag for the tweet.
        formatted_date (str): Should be "eng" or "esp".
        data (str): The path to the data file to be read.
        source (str): The data source.
        cleaner (bool): Indicates whether to clean the source file.

    Returns:
        str: The line to be tweeted.
    """
    try:
        text = read_file(data, cleaner)
        if formatted_date is None:
            text = f'{hashtag}: {text} {source}'
        else:
            text = f'{hashtag}, {formatted_date}, {text} {source}'
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
