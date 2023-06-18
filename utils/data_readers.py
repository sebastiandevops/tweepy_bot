#!/usr/bin/env python3

import random


def read_and_delete(data):

    with open(data, 'r') as filename:
        lines = filename.readlines()

    # Find the longest line
    # myline = max(lines, key=len)
    myline = random.choice(lines)

    lines.pop(lines.index(myline))

    with open(data, 'w') as filename:
        filename.writelines(lines)

    mystr = myline.strip()

    return mystr


def read(data):

    with open(data, 'r') as filename:
        lines = filename.readlines()

    # Find the longest line
    # myline = max(lines, key=len)
    myline = random.choice(lines)

    mystr = myline.strip()

    return mystr


if __name__ == '__main__':
    pass
