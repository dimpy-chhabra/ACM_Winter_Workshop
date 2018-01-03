from sklearn import cluster
import numpy as np
import pandas 
import matplotlib.pyplot as plt


data = pandas.read_csv('driver.csv', sep = '\t')
k = 2
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(data)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_
print centroids

for i in range(k):
    # select only data observations with cluster label == i
    ds = data[np.where(labels==i)]
    # plot the data observations
    pyplot.plot(ds[:,0],ds[:,1],'o')
    # plot the centroids
    lines = pyplot.plot(centroids[i,0],centroids[i,1],'kx')
    # make the centroid x's bigger
    pyplot.setp(lines,ms=15.0)
    pyplot.setp(lines,mew=2.0)
pyplot.show()
