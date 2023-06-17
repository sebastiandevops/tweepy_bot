#!/usr/bin/env python3

import random
from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal


def data_processor_start(data):

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

    return mystr


def data_processor_end(data):

    with open(data, 'r') as filename:
        lines = filename.readlines()

    myline = random.choice(lines)

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

    return mystr


def data_processor_english(data):

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

    return mystr


if __name__ == "__main__":
    pass
