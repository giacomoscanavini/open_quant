"""
Uniform Quotient
If a and b ~ U[0,1] what is the probability that a/b is in [1,3]?
"""

import numpy as np

N = 1000000
P = 0 

for _ in range(N):
    a,b = np.random.uniform(0, 1, size=2)
    if 1 < a/b < 3: 
        P +=1

print(f"P(1 < a/b < 3) = {P/N}")