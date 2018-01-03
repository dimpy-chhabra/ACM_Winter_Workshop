import tweepy
import time
import ques1
#insert your Twitter keys here
consumer_key = "..."
consumer_secret = "..."
access_token = "...-..."
access_secret = "..."

twitter_handle='AllCardsOut'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

list= open('twitter_followers.txt','w')

if(api.verify_credentials):
    print 'We successfully logged in'

user = tweepy.Cursor(api.followers, screen_name = twitter_handle).items()
followers=[]
while True:
    print("00")
    try:
        u = next(user)
        print(u.screen_name)
        followers.append(u.screen_name);
        #get_all_tweets(u)
        list.write(u.screen_name +' \n')
        
    except:
        for name in followers:
          ques1.get_all_tweets(name)
        time.sleep(15*60)
        print 'We got a timeout ... Sleeping for 15 minutes'
        u = next(user)
        list.write(u.screen_name +' \n')
list.close()
