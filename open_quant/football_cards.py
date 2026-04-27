"""
Football Cards
James has 6 packs of football cards. Each pack only contains 1 card inside. 
There are 10 distinct cards he can get, each of which is equally likely to appear in any pack. 
Find the expected number of distinct football cards that James obtains in the 6 packs.
"""

import numpy as np

N = 100000
n = 0

for _ in range(N):
    found = np.random.choice(list(range(1, 11)), size=6, replace=True)
    found = len(set(found))

    n += found

print(f"Expected number of unique cards = {n/N}")