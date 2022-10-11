'''2022.10.10'''
import numpy as np
import matplotlib.pyplot as plt

rand = np.random.RandomState(42)
X = rand.rand(10, 2)
#plt.scatter(X[:, 0], X[:, 1], s=100)
dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1)

nearest = np.argsort(dist_sq, axis=1)
K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)
plt.scatter(X[:, 0], X[:, 1], s=100)
print(nearest_partition)
for i in range(X.shape[0]) :
    for j in nearest_partition[i, :K+3] :
        plt.plot(*zip(X[j], X[i]), color='black')
