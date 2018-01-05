import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
import tweepy
from tweepy import OAuthHandler
import csv
from textblob import TextBlob
from datetime import datetime


consumer_key = "..."
consumer_secret = "..."
access_token = "..."
access_secret = "..."

twitter_handle='...'

auth=OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_secret)

api=tweepy.API(auth)
'''
    a. Length of tweet
    b. Number of hashtags in tweet
    c. Number of @ mentions in tweet
    d. Likes received by the tweet
    e. Retweets received by the tweet
    f/g. Sentiment expressed in the tweet (refer TextBlob API)
    h. Hour when tweet was posted, eg. If a tweet is posted at 7:35 pm, then hours = 19
'''

with open('%s_tweets_trial_tweets.csv' % twitter_handle, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["length","number_of_hashtags","number_of_mentions", "likes_received", "retweets_received", "sentiment_polarity", "sentiment.subjectivity", "time"])
    for tweet in tweepy.Cursor(api.user_timeline, id=twitter_handle, q='to%3ANASA&tweet_mode=extended').items(): 
        str = (tweet.text.encode("utf-8"))
        if(str[0:2]=="RT"):
            print ("Retweet")
        else:

            an = TextBlob(str)

            a = len(str)
            b = len(tweet._json['entities']['hashtags'])
            c = len(tweet._json['entities']['user_mentions'])
            d = tweet._json['favorite_count']
            e = tweet._json['retweet_count']
            f = an.sentiment.polarity
            g = an.sentiment.subjectivity
            s2 = tweet._json['created_at'][0:19]
            h = datetime.strptime(s2,'%a %b %d %H:%M:%S').strftime('%H')
            outtweets = [a,b,c,d,e,f,g,h]
            writer.writerow(outtweets)
            