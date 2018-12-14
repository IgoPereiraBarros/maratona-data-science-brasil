import json
from requests_oauthlib import OAuth1Session
import urllib

MAX_TWEETS = 100
BASE_URL = 'https://api.twitter.com/1.1/search/tweets.json'
BASE_URL_MESSAGE = 'https://api.twitter.com/1.1/statuses/update.json'

class TwitterClient(object):

    def __init__(self, consumer_key, consumer_secret, access_token, access_secret_token):
        self.__CONSUMER_KEY = consumer_key
        self.__CONSUMER_SECRET = consumer_secret
        self.__ACCESS_TOKEN = access_token
        self.__ACCESS_SECREAT_TOKEN = access_secret_token

        self.__session = OAuth1Session(self.__CONSUMER_KEY,
                                    self.__CONSUMER_SECRET,
                                    self.__ACCESS_TOKEN,
                                    self.__ACCESS_SECREAT_TOKEN)

    def search(self, search_tweet, safe=''):
        return urllib.parse.quote(search_tweet, safe)

    def get_tweets(self, keyword, n=15, lang='pt', max_id=None):
        if n > 0:
            url = BASE_URL + '?q={}&count={}'.format(keyword, n)
            #if max_id is not None:
                #url = url + '&max_id={}'.format(max_id)
            if lang is not 'pt':
                url = url + '&lang={}'.format(lang)
            response = self.__session.get(url)
            if response.status_code == 200:
                tweets = json.loads(response.content)
                #oldest_id = [tweet for tweet in tweets['statuses']]
                return tweets['statuses'] # + self.get_tweets(keyword, n-MAX_TWEETS, oldest_id)
        return []

    def post_message(self, message):
        url = BASE_URL_MESSAGE + '?status={}'.format(message)
        response = self.__session.post(url)
        twees_message = json.loads(response.content)
        return twees_message
