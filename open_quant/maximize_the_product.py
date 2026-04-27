"""
Maximize the Product
1) Suppose you roll two fair 6-sided dice. 
What is the expected value of the product of the two dice?

2) Suppose you have the two fair 6-sided dice and you are trying to 
maximize the product with an optional re-roll. 
What is the expected value with optimal play?
"""

import numpy as np

n = 0
N = 1000000

for _ in range(N):
    d1, d2 = np.random.choice(list(range(1, 7)), size=2, replace=True)
    product = d1 * d2

    if product < 12.25:
        d1 = max(d1, d2)
        d2 = np.random.choice(list(range(1, 7)))

    n += d1 * d2

print(f"Expected product with 1 reroll = {n/N}")