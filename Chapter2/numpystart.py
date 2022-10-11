'''2022.10 Data science study'''
import numpy as np
import matplotlib.pyplot as plt
import seaborn
rand = np.random.RandomState(42)   # pylint: disable=E1101

mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)

seaborn.set()
plt.scatter(X[:, 0], X[:, 1])

indices = np.random.choice(X.shape[0], 20, replace=False)

selection = X[indices]
plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1], facecolor='none', s=200)

x = np.arrange(10)