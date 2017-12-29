#Linear_Models
#Logistic Regression
#Machine Learning Type: Classification
#http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target


estimator = LogisticRegression(verbose =1, max_iter=100)

estimator.fit(X,y)

t = [[5.4, 3.9, 2.6, 1.0], [2.4, 1.4, 1.6, 3.2] ]
print "Predictions:"
print( estimator.predict(t) )
