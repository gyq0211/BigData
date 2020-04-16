import socket
import sys
import requests
import requests_oauthlib
import json
import tweepy

consumer_key = 'ujqZDsYNaxDr5o0NP5ebYMioH'
consumer_secret = 'wdKwKxFYXGdTWlAeF6EnsAKnd2YKvkYedT659Rt8M0qViSyqSM'
access_token = '1194778777894576128-SQeZJ39Z23hV164fkBAJnB001Sp7yZ'
access_token_secret = 'cNdRczrHwOwBckrVapY4oiLFVp5Y5n0pyLDyOor1yP68d'
auth = requests_oauthlib.OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
API = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def get_tweets():
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    query_data = [('language', 'en'), ('locations', '-130,-20,100,50'), ('track', '#')]
    query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
    response = requests.get(query_url, auth=auth, stream=True)
    print(query_url, response)
    return response


"""def get_tweets():
    public_tweets = API.home_timeline()
    for tweet in public_tweets[:1]:
        print(show_tweet(tweet))
    return show_tweet(tweet)"""


def send_tweets_to_spark(http_resp, tcp_connection):
    for line in http_resp.iter_lines():
        try:
            full_tweet = json.loads(line)
            tweet_text = full_tweet['text']
            print("Tweet Text: " + tweet_text)
            print("------------------------------------------")
            tcp_connection.send(tweet_text + '\n')
        except:
            e = sys.exc_info()[0]
            print("Error: %s" % e)


#TCP_IP = " "
TCP_PORT = 9009
conn = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))
s.listen(1)
print("Waiting for TCP connection...")
conn, addr = s.accept()
print("Connected... Starting getting tweets.")
resp = get_tweets()
send_tweets_to_spark(resp, conn)



"""def show_tweet(tweet):
    try:
        return ' '.join([tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                         tweet.user.screen_name,
                         tweet.text])
    except:
        return '************************ bad or no tweet ************************'


class Listener(tweepy.streaming.StreamListener):

    def __init__(self, output_file=sys.stdout):
        super(Listener, self).__init__()
        self.output_file = output_file

    def on_status(self, tweet):
        print(show_tweet(tweet), file=self.output_file)

    def on_error(self, status_code):
        print(status_code)
        return False


listener = Listener(conn)"""
#print('Starting!!!!!!!!!!!!!!!!!!')


"""try:
    #data = open("gs://bigdata-quiz4/todo1.txt", 'w+')
    data = open("/Users/yunqigao/Downloads/yunqi.txt", 'w+')
    print('Start streaming.')
    #tweeters = API.followers(id="nytimes")
    tweeters = API.home_timeline(id="Yunqi30749134")
    for tweet in public_tweets:
        print(tweet.text)
        print(tweet.text , file = data)
    #stream.filter(follow=tweeters)
    #for i in range(20):
        #print(tweeters[i])
        #print(tweeters[i] , file = data)
    data.close()
except KeyboardInterrupt:
    print("Stopped.")
finally:
    #stream.disconnect()
    print('Done.')"""
