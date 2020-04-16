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
API = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def show_tweet(tweet):
    try:
        return ' '.join([tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                         tweet.user.screen_name,
                         tweet.text])
    except:
        return '************************ bad or no tweet ************************'


public_tweets = API.home_timeline()

print('Starting!!!!!!!!!!!!!!!!!!')


try:
    print('Start streaming.')
    tweeters = API.followers(id="nytimes")
    for i in range(20):
        print(tweeters[i])
except KeyboardInterrupt:
    print("Stopped.")
finally:
    print('Done.')
