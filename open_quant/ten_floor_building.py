"""
Ten Floor Building
A building has 10 floors above the basement. 
If 12 people get into an elevator at the basement, 
and each chooses a floor at random to get out, 
independently of the others, at how many floors do 
you expect the elevator to make a stop to let out one or more of these 12 people?
"""

import numpy as np

floors = list(range(1, 11))

N = 100000
n = 0

for _ in range(N):
    selected = np.random.choice(floors, size=12, replace=True)
    selected = len(set(selected))
    n += selected

print(f"Expected number of selected floors = {n/N}")