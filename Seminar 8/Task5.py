from math import factorial
n, p = 0, 0
while p < 0.5:
    n += 1
    p = 1 - factorial(365)/(365**n*factorial(365-n))
print(n)
