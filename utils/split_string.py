#!/usr/bin/env python3

def split_string(string):
    if len(string) > 240:
        first_string = string[:240]  # First 240 characters
        second_string = string[240:]  # Remaining characters
    else:
        first_string = string
        second_string = ""

    return first_string, second_string
