data <- read.csv("iris.csv")
myTable <- table(data$class)
print (myTable)
lbls <-paste(names(myTable), " \n ", myTable, sep="")
print (lbls)
pie(myTable, labels = lbls, main="Pie Chart of Species\n (with sample sizes)")
png(file = "pie.png")

