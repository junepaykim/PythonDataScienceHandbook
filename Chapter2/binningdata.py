'''binning data 2022.10.10'''
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.randn(100)

bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

i = np.searchsorted(bins, x)

np.add.at(counts, i, 1)

plt.plot(bins, counts, linestyle='solid')

plt.hist(x, bins, histtype='step')