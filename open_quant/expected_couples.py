"""
Expected Couples
Eight people from four married couples are randomly assigned to seats 
around a round table. What is the expected number of 
couples that are seated next to each other?
"""

import numpy as np

people = list('aabbccdd')
N = 100000
n = 0

for _ in range(N):
    seats = np.random.choice(people, size=8, replace=False).tolist()

    for p1, p2 in zip(seats[:], seats[1:] + list(seats[0])):
        if p1 == p2: 
            n += 1
    
print(f"Expected number of couples sitting together = {n/N}")