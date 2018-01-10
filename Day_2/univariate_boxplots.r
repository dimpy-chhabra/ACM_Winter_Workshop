data <- read.csv("trump_tweets.csv")

	a <- data$length
	b <- data$number_of_hashtags
	c <- data$number_of_mentions
	d <- data$likes_received
	e <- data$retweets_received
	f <- data$sentiment_polarity
	g <- data$sentiment.subjectivity
	h <- data$time

scatter.smooth(x=c, y=d, main="number_of_mentions ~ likes_received")  # scatterplot(Bivariate)

par(mfrow=c(1, 2))  # divide graph area in 2 columns

boxplot(c, main="number_of_mentions", sub=paste("Outlier rows: ", boxplot.stats(c)$out))  # box plot for 'speed' (Univariate)

boxplot(d, main="likes_received", sub=paste("Outlier rows: ", boxplot.stats(d)$out))  # box plot for 'distance' (Univariate)

linearMod <- lm(dist ~ speed, data=data)  # build linear regression model on full data

print(linearMod)
