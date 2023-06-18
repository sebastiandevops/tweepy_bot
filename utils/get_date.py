#!/usr/bin/env python3

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal


def get_date_spanish():
    # Get the current date
    current_date = datetime.now()

    # Format the date components separately
    day = format_decimal(current_date.day, format='##')
    month = format_date(current_date, format='MMMM', locale='es')

    # Format the date as "month day"
    # Create the formatted date with "de" separator
    formatted_date = f"{day} de {month}"

    return formatted_date


def get_date_english():
    # Get the current date
    current_date = datetime.now()

    # Format the date as "month day"
    formatted_date = current_date.strftime("%B %d")

    return formatted_date
