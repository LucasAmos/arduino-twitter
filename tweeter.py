#!/usr/bin/env python

# Python script to retrive the latest tweet from a user
# Created by zone13.io (https://www.zone13.io)
# Version 1.0
# Usage - ./script.py <twitter_handle>
# e.g. ./script.py rihanna
# Adapted from https://github.com/bear/python-twitter

# Requirement - pip install python-twitter
import unicodedata
import sys, twitter
import time, datetime, pytz, calendar


api = twitter.Api()

# Populate your twitter API details below

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret
)


def user_tweet(thandle):
    statuses = api.GetUserTimeline(screen_name=thandle)

    text = statuses[0].text
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode("utf-8")

    ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(statuses[0].created_at, '%a %b %d %H:%M:%S +0000 %Y'))
    ts = time.strptime(ts,'%Y-%m-%d %H:%M:%S')
    ts = calendar.timegm(ts)

    tweet = {'createdAt': ts, 'text': text}
    return tweet


if __name__ == "__main__":
    latest_tweet = user_tweet(sys.argv[1])
    print(latest_tweet)


