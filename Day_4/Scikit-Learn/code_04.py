#Support vector machines
#Multi-class classification
#Machine Learning Type: Classification
#http://scikit-learn.org/stable/modules/svm.html

from sklearn import svm

X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')

clf.fit(X, Y)

dec = clf.decision_function([[1]])
print(dec.shape[1])

clf.decision_function_shape = "ovr"
dec = clf.decision_function([[1]])
print(dec.shape[1]) 
