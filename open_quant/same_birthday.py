"""
Same Birthday
If you have N people in a room, 
what is the likelihood that at least 2 of them have the same birthday?
"""

import numpy as np
from collections import Counter

n = 100000

for N in range(10, 30):
    P = 0
    for _ in range(n):
        bdays  = np.random.randint(1, 366, size=N)
        counts = Counter(bdays).values()
        counts = np.array([x for x in counts])

        for i in counts: 
            if i > 1: 
                P += 1
                break
        
    print(f"N = {N}, P(At least 2 birthdays) = {P/n}")
