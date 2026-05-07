"""
Find the Variance
What is the variance of a uniform random variable X with probability density function 
f(x) = 1 for 0 ≤ x ≤ 1 and zero elsewhere?
"""

import numpy as np

N = 100000
X = np.random.uniform(0, 1, size=N)
mean = np.mean(X)
variance = np.var(X)

print(f"E[X] = {round(mean, 3)}")
print(f"Var(X) = {round(variance, 3)}")