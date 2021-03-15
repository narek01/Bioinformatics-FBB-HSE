import numpy as np
from scipy.stats import uniform

rv = uniform(0, 1)
x = rv.rvs(size=10000000)
f = np.sinh(x) + np.cosh(x) + 1
print(np.mean(f))
