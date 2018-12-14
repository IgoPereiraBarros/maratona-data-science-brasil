# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import requests
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret_token = ''

session = OAuth1Session(consumer_key, consumer_secret, access_token, access_secret_token)

url = "https://api.twitter.com/1.1/search/tweets.json?q={}".format(requests.utils.quote('#neji'))
response = session.get(url)

tweets = json.loads(response.content)

for t in sorted(tweets["statuses"], key=lambda x: x["retweet_count"], reverse=True):
    print (t["text"])
