"""
Three Sticks
Assume you are given a stick that is 1 meter in length. 
Randomly select 2 points on the stick and break it at these 2 points to get 3 pieces. 
What's the probability that the smallest piece is at most 0.2 meter?
"""

import numpy as np

P = 0
N = 1000000

for _ in range(N):
    x1, x2 = np.random.uniform(0, 1, size=2)

    if x2 > x1:
        z = min(x1, x2-x1, 1-x2)
    else:
        z = min(x2, x1-x2, 1-x1)
    
    if z <= 0.2:
        P += 1

print(f"Probability min(l1, l2, l3) <= 0.2) = {P/N}")