data <- read.csv("iris.csv")

getmode <- function(v) {
   uniqv <- unique(v)
   uniqv[which.max(tabulate(match(v, uniqv)))]
}


print("Mean: ")

print(mean(data$petallength))
print(mean(data$petalwidth))
print(mean(data$sepallength))
print(mean(data$sepalwidth))

print("Median: ")

print(median(data$sepalwidth, na.rm = FALSE))

print("Mode: ")

print(getmode(data$petallength))
