"""
Maximize the Product
1) Suppose you roll two fair 6-sided dice. 
What is the expected value of the product of the two dice?

2) Suppose you have the two fair 6-sided dice and you are trying to 
maximize the product with an optional re-roll. 
What is the expected value with optimal play?
"""

import numpy as np

n1 = 0
n2 = 0
N = 100000

for _ in range(N):
    rolls = np.random.choice(list(range(1, 7)), size=2, replace=True)
    d1, d2 = max(rolls), min(rolls)

    n1 += d1 * d2
    
    if d2 < 3.5: 
        d2 = np.random.choice(list(range(1, 7)))

    n2 += d1 * d2

print(f"1) Expected product without reroll = {n1/N}")
print(f"2) Expected product with 1 reroll = {n2/N}")