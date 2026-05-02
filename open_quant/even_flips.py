"""
Even Flips
Paul flips a fair coin until he obtains two consecutive heads or tails 
for the first time. Find the probability Paul flips the coin an even number of times.
"""

import numpy as np

P = 0
N = 100_000

for _ in range(N):
    previous = -1
    n = 0
    while 1:
        roll = np.random.choice([0, 1])
        n += 1
        if roll == previous:
            if n & 1 == 0:
                P += 1
            break
        else:
            previous = roll

print(f"Probability HH or TT on even flips = {P/N}")


        