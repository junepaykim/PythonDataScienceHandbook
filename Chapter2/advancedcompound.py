'''compound practice'''
import numpy as np

tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3,3))])
X = np.zeros(2, dtype=tp)
print(X[0])
print(X['mat'][1])
