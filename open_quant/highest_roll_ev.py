"""
Highest Roll EV
Jim will roll a fair, six-sided die until he gets a 4. 
What is the expected value of the highest number he rolls through this process?
"""

import numpy as np

N = 1_000_000
E = 0

for _ in range(N):
    highest = 0
    while 1:
        roll = np.random.choice(list(range(1, 7)))
        if roll > highest:
            highest = roll
        if roll == 4:
            break

    E += highest

print(f"Expected highest roll given seeing a 4 = {E/N}")