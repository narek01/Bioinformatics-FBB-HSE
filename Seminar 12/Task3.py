import numpy as np
from scipy.stats import ttest_rel, ttest_ind

X = [0.02, 0.1, 0.2, 0.7, 0.5]
Y = [0.9, 0.8, 0.9, 0.6, 0.4]

print("X: ", X, "mean is", np.mean(X), "\nY: ", Y, "mean is", np.mean(Y))
print("\nPair: ", round(ttest_rel(X, Y).pvalue, 3))
print("Unpair: ", round(ttest_ind(X, Y).pvalue, 3))


switch = False
#switch = True

while switch:
    X = np.random.sample(5)
    Y = np.random.sample(5)
    if ttest_rel(X, Y).pvalue > 0.1 and ttest_ind(X, Y).pvalue < 0.05:
        print("X: ", X)
        print("Y: ", Y)
        print("\nPair: ", round(ttest_rel(X, Y).pvalue, 3))
        print("Unpair: ", round(ttest_ind(X, Y).pvalue, 3))
        switch = False
