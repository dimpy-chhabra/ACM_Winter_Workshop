import numpy as np
from sklearn.cluster import KMeans
import pandas 
import matplotlib.pyplot as plt

### For the purposes of this example, we store feature data from our
### dataframe `df`, in the `f1` and `f2` arrays. We combine this into
### a feature matrix `X` before entering it into the algorithm.

data_df = pandas.read_csv('driver.csv', sep = '\t')
#print(data_df)
f1 = data_df['Distance_Feature'].values
f2 = data_df['Speeding_Feature'].values

X=np.matrix(zip(f1,f2))
kmeans = KMeans(n_clusters = 2).fit(X)

print(kmeans.labels_)
print(kmeans.cluster_centers_)


plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='black', s=200, alpha=0.5);

