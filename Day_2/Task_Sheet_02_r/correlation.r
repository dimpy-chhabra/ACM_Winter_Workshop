#Question 2.
#Find correlation between all pairs of attributes
#PieChart
#LineChart

data <- read.csv("iris.csv")

print(cor(data$petallength, data$petalwidth))

print(cor(data$petallength, data$sepallength))
print(cor(data$petallength, data$sepallength))
print(cor(data$sepallength, data$petalwidth))
print(cor(data$sepallength, data$sepalwidth))
print(cor(data$sepalwidth, data$petalwidth))


plot(x = data$petallength , y = data$petalwidth)
boxplot(data$petallength)

png(file = "boxplot.png")

#pie(x = data$class)

