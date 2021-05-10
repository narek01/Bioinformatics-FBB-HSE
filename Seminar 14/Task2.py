import numpy as np
from scipy.stats import spearmanr, pearsonr

#X = np.random.uniform(16, 1.00000000001, 98)
#Y = np.random.uniform(1, 1.00000000001, 98)

X, Y = [], []
for i in range(1, 99):
    X.append(-i)
    Y.append(i)

X = np.insert(X, 0, -10000000)
X = np.insert(X, 99, 10000000)
Y = np.insert(Y, 0, -10000000)
Y = np.insert(Y, 99, 10000000)

print("X: ", X)
print("Y: ", Y)
print("\nPearson: ", round(pearsonr(X, Y)[0], 2), "(> 0.9)")
print("Spearman: ", round(spearmanr(X, Y)[0], 2), "(< 0.1)")


'''

'''
