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

consumer_key = 'kgGtb2Exedpdt95rxjmDH226b'
consumer_secret = 'Xp5MorhSVi4bmY9JvCrnnEulGsl5LOEn7esUKGBvy0tGh5VzsT'
access_token_key = '910943517136089088-4eaC7ivHJhv6S0O9sboMAYaozy9lXVs'
access_token_secret = 'lbYf3Tqg2oUCUFQb03l1MNQ6n1RtFnGotVFUTH6EsI8qX'

api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret
)


def user_tweet(thandle):
    statuses = api.GetUserTimeline(screen_name=thandle)

    text = statuses[0].fulltext
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode("utf-8")

    ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(statuses[0].created_at, '%a %b %d %H:%M:%S +0000 %Y'))
    ts = time.strptime(ts,'%Y-%m-%d %H:%M:%S')
    ts = calendar.timegm(ts)

    tweet = {'createdAt': ts, 'text': text}
    return tweet


if __name__ == "__main__":
    latest_tweet = user_tweet(sys.argv[1])
    print(latest_tweet)


