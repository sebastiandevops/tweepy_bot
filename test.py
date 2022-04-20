#!/usr/bin/python3
import random
# Authenticate to Twitter

def remove_line(fileName,lineToSkip):
    """ Removes a given line from a file """
    with open(fileName,'r') as read_file:
        lines = read_file.readlines()

    currentLine = 1
    with open(fileName,'w') as write_file:
        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)

            currentLine += 1


def tweet_job():
    with open('/home/sebastian/estudio/tweepy_bot/sample.txt','r') as filename:
        lines = filename.readlines()

    myline =random.choice(lines)
    line_no = lines.index(myline)
    print(line_no)

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    mystr = myline.replace("\n"," ")
    content = mystr
    print(mystr)

tweet_job()
