#Question 2.
#Find correlation between all pairs of attributes
#PieChart
#LineChart


data <- read.csv("trump_tweets.csv")

	b <- data$number_of_hashtags
	c <- data$number_of_mentions
	d <- data$likes_received
	e <- data$retweets_received

print(cor( b, d))
print(cor( c, d))
print(cor( b, e))
print(cor( c, e))
