import numpy as np
import tweepy
# accessing the twitter API

consumer_key = 'ujqZDsYNaxDr5o0NP5ebYMioH'
consumer_secret = 'wdKwKxFYXGdTWlAeF6EnsAKnd2YKvkYedT659Rt8M0qViSyqSM'
access_token = '1194778777894576128-SQeZJ39Z23hV164fkBAJnB001Sp7yZ'
access_token_secret = 'cNdRczrHwOwBckrVapY4oiLFVp5Y5n0pyLDyOor1yP68d'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# importing data from afinn dict

#sc = SparkContext()
# create the Streaming Context from the above spark context with interval size 2 seconds
#ssc = StreamingContext(sc, 2)
# read data from port 9009
#tweets = ssc.socketTextStream("localhost", 9009)

class color:
    PURPLE = '\033[95m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


d = {}
file = open(r"/Users/yunqigao/Downloads/AFINN-en-165.txt")
#file = open("gs://bigdata-quiz4/AFINN-en-165.txt", "r")
#file = open("hdfs://user/gyq/AFINN-en-165.txt", "r")
for line in file:
    ' '.join(line.split())
    x = line.split()
    #print(x)
    d[x[0]] = int(x[len(x) - 1])

#print(d)


def checkKey(dict, key):
    if key in dict:
        return 1
    else:
        return 0


rating = 0
ratings = {}
ratings = list()
tweets = {}
tweets = list()
sumrate = 0
num_item =100
# importing tweets
# demonitisation 2000
for tweet in tweepy.Cursor(api.search, q='yunqi' + ' -RT', since="2019-09-01", lang="en").items(num_item):
    text = tweet.text.lower()
    for word in text.split():
        if (checkKey(d, word) == 1):
            rating = rating + int(float(d[word]))
    print("\n", text)
    print("rating of tweet=", rating)
    ratings.append(rating)
    sumrate = sumrate + rating
    tweets.append(text)
    rating = 0
ratings = np.array(ratings)
print(color.YELLOW , "here is the average sentiment of tweeter:")
print(color.YELLOW , sumrate/num_item)
# finding top 5 positive and negative tweets
top_5_index = np.argsort(ratings)[-5:]

print("##########################TOP#############################")
print(color.BLUE, "TOP 5 POSITIVE TWEETS\n")
for i in range(0, len(top_5_index)):
    print(tweets[top_5_index[i]])
    print(color.BLUE, "tweet rating=", ratings[top_5_index[i]])
    print("\n")

worst_5_index = ratings.argsort()[:5]
print(color.PURPLE, "TOP 5 NEGATIVE TWEETS\n")
for i in range(0, len(worst_5_index)):
    print(tweets[worst_5_index[i]])
    print(color.PURPLE, "tweet rating=", ratings[worst_5_index[i]])
    print("\n")

# finding total no of tweets and positive , neg, neutral tweets
pos_count = 0
neg_count = 0
zero_count = 0
for num in ratings:
    if num == 0:
        zero_count += 1
    elif num < 0:
        neg_count += 1
    else:
        pos_count += 1

print(color.GREEN, "total number of tweets=", len(ratings))
print(color.GREEN, "total number of positive tweets=", pos_count)
print(color.GREEN, "total number of negative tweets=", neg_count)
print(color.GREEN, "total number of neutral tweets=", zero_count)
