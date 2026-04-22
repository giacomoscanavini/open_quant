"""
Normal Distributions
Consider that X and Y are independent standard normal random variables. 
What is the P[Y > 4X]?
"""

import numpy as np

N = 100000

x = np.random.normal(loc=0, scale=1, size=N)
y = np.random.normal(loc=0, scale=1, size=N)
P = [1 for val1, val2 in zip(x,y) if val2 > 4*val1]

z = [val2 - 4*val1 for val1, val2 in zip(x,y)]
mean = np.mean(z)
var = np.var(z)

print(f"P[Y > 4X] = {sum(P)/N}")
print(f"E[Y - 4X] = {mean}")
print(f"Var(Y - 4X) = {var}")