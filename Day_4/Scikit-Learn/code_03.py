#Support vector machines
#Module
#Machine Learning Type: Classification
#http://scikit-learn.org/stable/modules/svm.html


from sklearn import svm


X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()

#The better your features, the better your accuracy

clf.fit(X, y)
S = [[0.3, 0.7], [1, 0]]
print(clf.predict(S))
