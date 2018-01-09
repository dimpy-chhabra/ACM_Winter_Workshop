import numpy as np
import matplotlib.pyplot as plt
import csv

data = pd.read_csv('trump_tweets.csv')
a = data.length
b = data.number_of_hashtags
c = data.number_of_mentions
d = data.likes_received
e = data.retweets_received
f = data.sentiment_polarity
g = data.sentiment.subjectivity
h = data.time

data = 500
labs = 500

grey_height = 28 + 4*np.random.randn(greyhounds)
lab_height = 24 + 4*np.random.randn(labs)

plt.hist([a, d], stacked =False, color=['r','b'])
#Stacked: Refers to the presence of the two features getting plotted one over the other or sidewise.
plt.show()
