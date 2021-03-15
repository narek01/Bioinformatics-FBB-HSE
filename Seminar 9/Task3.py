from scipy.stats import uniform

# Вариант курильщика
uniform_rv = lambda a, b: (b - a) * uniform().rvs() + a

# Вариант адекватный
def uniform_rv(a, b):
    random_value = uniform().rvs()
    return (b - a) * random_value + a
