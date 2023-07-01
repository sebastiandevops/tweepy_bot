#!/usr/bin/env python3

import random


def get_line(hashtag, formatted_date, data, line, source, cleaner):
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
        text = read_file(data, line, cleaner)
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


def read_file(data, line, cleaner):
    """
    Read the file and optionally clean the line if cleaner is True.

    Args:
        data (str): The data to read from the file.
        line: The desired line. It can be either "longest" or "random".
              Default is None. If None, the tweet line will be random.
        cleaner (bool): Indicates whether to clean the source file.

    Returns:
        str: The text to populate the tweet.
    """
    with open(data, 'r') as filename:
        lines = filename.readlines()
    try:
        if line == "longest":
            # Find the longest line
            if len(lines) > 1:
                myline = max(lines, key=len)
            elif len(lines) == 1:
                myline = lines[0]
            else:
                raise ValueError("No lines found in the file.")
        elif line == "random" or line is None:
            if len(lines) > 0:
                myline = random.choice(lines)
            else:
                raise ValueError("No lines found in the file.")
    except ValueError as e:
        e = "line should be either random, longest or None"
        print(f"Error: {e}")
        myline = ""

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
