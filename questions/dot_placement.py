"""
Dot Placement
You place three dots along the edges of an octagon at random
What is the probability that all three dots lie on distinct edges of the octagon?
"""

import numpy as np

N = 100000
edges = list(range(1, 9))
n = 3

P = 0
for _ in range(N):
    dots = np.random.choice(edges, size=n, replace=True)
    if len(np.unique(dots)) == n: 
        P += 1

print(f"Probability all three dots lie on distinct edges of the octagon = {P/N}")
