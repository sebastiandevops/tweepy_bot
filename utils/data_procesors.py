#!/usr/bin/env python3

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal
from utils.data_readers import read_and_delete, read


def get_line_start(data, source):

    mystr = read_and_delete(data)

    # Get the current date
    current_date = datetime.now()

    # Format the date components separately
    day = format_decimal(current_date.day, format='##')
    month = format_date(current_date, format='MMMM', locale='es')

    # Format the date as "month day"
    # Create the formatted date with "de" separator
    formatted_date = f"{day} de {month}"

    mystr = f'🤖 #HoyEnLaHistoria, {formatted_date}, {mystr} {source}'

    return mystr


def get_line_end(data, source):

    mystr = read(data)
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
    mystr = f'🤖 #HoyEnLaHistoria, {formatted_date}, {mystr} {source}'

    return mystr


def get_line_english(data, source):

    mystr = read(data)

    # Get the current date
    current_date = datetime.now()

    # Format the date as "month day"
    formatted_date = current_date.strftime("%B %d")

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    mystr = f'🤖 #OnThisDay, {formatted_date}, {mystr} {source}'

    return mystr


def get_line_english_start(data, source):

    mystr = read_and_delete(data)

    # Get the current date
    current_date = datetime.now()

    # Format the date as "month day"
    formatted_date = current_date.strftime("%B %d")

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    mystr = f'🤖 #OnThisDay, {formatted_date}, {mystr} {source}'

    return mystr


if __name__ == "__main__":
    pass
