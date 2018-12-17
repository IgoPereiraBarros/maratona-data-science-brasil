from twitter import TwitterClient
import pprint

CONSUMER_KEY = 'your key'
CONSUMER_SECRET = 'your key'
ACCESS_TOKEN = 'your token'
ACCESS_SECREAT_TOKEN = 'your token'

client = TwitterClient(CONSUMER_KEY, CONSUMER_SECRET,
                       ACCESS_TOKEN, ACCESS_SECREAT_TOKEN)

pesquisar = client.search('#naruto')

#get_msg = client.post_message(pesquisar)

tweets = client.get_tweets(pesquisar, n=100, lang='pt')

for tweet in tweets:
    pprint.pprint(tweet['text'])
