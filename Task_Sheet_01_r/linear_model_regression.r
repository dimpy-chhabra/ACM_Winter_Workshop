head(cars)

scatter.smooth(x=cars$speed, y=cars$dist, main="Dist ~ Speed")  # scatterplot(Bivariate)

par(mfrow=c(1, 2))  # divide graph area in 2 columns

boxplot(cars$speed, main="Speed", sub=paste("Outlier rows: ", boxplot.stats(cars$speed)$out))  # box plot for 'speed' (Univariate)

boxplot(cars$dist, main="Distance", sub=paste("Outlier rows: ", boxplot.stats(cars$dist)$out))  # box plot for 'distance' (Univariate)

linearMod <- lm(dist ~ speed, data=cars)  # build linear regression model on full data

print(linearMod)

#dist = −17.579 + 3.932∗speed
