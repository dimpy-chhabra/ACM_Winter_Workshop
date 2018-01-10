import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
import tweepy
from tweepy import OAuthHandler
import csv
from textblob import TextBlob
from datetime import datetime
'''
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""
twitter_handle=''
'''
consumer_key = "lSOxvZKPuvnOOxQHh6cMGY96q"
consumer_secret = "MPPrax16SZCJwiKzwtrFsPUGHs371CdR1cG3cV64n84SbdI9mq"
access_token = "949715346037948416-yXcxV0bECyTSCFA2RJrigL1D0eSiDzl"
access_secret = "d9BLKBhnbiNhSUP14asYJQg818NXhBemzpeI6V7LaGpGL"
twitter_handle='realDonaldTrump'

auth=OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_secret)

api=tweepy.API(auth)


with open('%s_tweets_trial_tweets.csv' % twitter_handle, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["length","number_of_hashtags","number_of_mentions", "likes_received", "retweets_received", "sentiment", "time", "hashtags_tuple", "hashtag_1", "hashtag_2", "hashtag_3", "hashtag_4", "hashtag_5"])
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
            #f = an.sentiment.polarity
            f = 'positive' if an.sentiment.polarity>0 else ('negative' if an.sentiment.polarity<0 else 'neutral')
            #g = an.sentiment.subjectivity
            s2 = tweet._json['created_at'][0:19]
            g = datetime.strptime(s2,'%a %b %d %H:%M:%S').strftime('%H')
            h = tweet._json['entities']['hashtags']
            le = len(h)
            if h:
            	outtweets = [a,b,c,d,e,f,g,h]
            	iter_ = 0
            	for iter in range(le):
            		s = h[iter]
            		i = s['text']
            		outtweets.append(i)
            	writer.writerow(outtweets)
            else:
            	outtweets = [a,b,c,d,e,f,g,h]
            	writer.writerow(outtweets)