import sys
import tweepy
import time
from tweepy import API
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# , access_token_secret
#auth = tweepy.OAuthHandler(_creds["consumer_key"], _creds["consumer_secret"]) auth.set_access_token(_creds["access_token"], _creds["access_token_secret"]) del _creds # delete _creds immediately!
API = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#API = tweepy.API(auth)

def show_tweet(tweet):
    try:
        return ' '.join([tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                         tweet.user.screen_name,
                         tweet.text])
    except:
        return '************************ bad or no tweet ************************'


public_tweets = API.home_timeline()
#for tweet in public_tweets[:1]:
    #print(show_tweet(tweet))


"""class Listener(tweepy.streaming.StreamListener):

    def __init__(self, output_file=sys.stdout):
        super(Listener, self).__init__()
        self.output_file = output_file

    def on_status(self, tweet):
        print(show_tweet(tweet), file=self.output_file)

    def on_error(self, status_code):
        print(status_code)
        return False


listener = Listener()"""
#stream = tweepy.Stream(auth=API.auth, listener=listener)
print('Starting!!!!!!!!!!!!!!!!!!')
# stream.filter(follow=[nyt.id_str])


try:
    #data = open("gs://bigdata-quiz4/todo1.txt", 'w+')
    #data = open("/home/yunqigaoyg/outp1.txt", 'w+')
    print('Start streaming.')
    tweeters = API.followers(id="nytimes")
    #stream.filter(follow=tweeters)
    for i in range(20):
        #print(tweeters[i])
        print(tweeters[i])
    #data.close()
except KeyboardInterrupt:
    print("Stopped.")
finally:
    #stream.disconnect()
    print('Done.')
