from sklearn.datasets import load_iris
iris = load_iris()
#
print iris.feature_names
print iris.target_names
print iris.data[0]
#The class for entry nuber 110:
print iris.target[110]

for i in range(len(iris.target)):
	print "Example %d: label %s, features %s" %(i, iris.target[i], iris.data[i])
