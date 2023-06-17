#!/usr/bin/env python3

from utils.split_string import split_string


def create_tweet(api, mystr):

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


if __name__ == "__main__":
    pass
