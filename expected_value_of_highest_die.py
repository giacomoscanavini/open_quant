"""
Expected Value of Highest Die
You roll two dice and select the one with the highest roll. 
What is the expected value of the die you selected?
"""

import numpy as np

D = list(range(1, 7))
N = 100000
E = 0

for _ in range(N):
    rolls = np.random.choice(D, size=2, replace=True)
    E += max(rolls)

print(f"Expected value of highest roll = {E/N}")