import numpy as np
from scipy.stats import spearmanr, pearsonr

X, Y = [], []
for i in range(1, 101):
    X.append(-1/i)
    Y.append(i**2)

print("X: ", X)
print("Y: ", Y)
print("\nPearson: ", round(pearsonr(X, Y)[0], 2), "(< 0.5)")
print("Spearman: ", round(spearmanr(X, Y)[0], 2), "(= 1)")
