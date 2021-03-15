import numpy as np
from scipy.stats import uniform

rv = uniform(-1, 1)
x = rv.rvs(size=10000000)
f = 1 / np.sqrt(1 - x**2)
print(2*np.mean(f))
