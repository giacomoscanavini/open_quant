"""
Good Grid
Suppose that two integers a and b are uniformly at random selected from 
S = {-10, -9, ..., 0, ..., 9, 10}
Find the probability that max(0,a) = min(0,b)
"""

import numpy as np

S = list(range(-10, 11))
N = 100000

P = 0
for _ in range(N):
    a, b = np.random.choice(S, size=2, replace=True)
    if np.max([0, a]) == np.min([0, b]):
        P += 1

print(f"Probability max(0,a) = min(0,b) = {P/N}")