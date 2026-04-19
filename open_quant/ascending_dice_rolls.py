"""
Ascending Dice Rolls
You throw three fair dice consecutively. 
What is the probability that you obtain three numbers in strictly increasing order?
"""

import numpy as np

N = 100000
S = list(range(1, 7))
P = 0

for _ in range(N):
    rolls = np.random.choice(S, size=3, replace=True)
    if rolls[0] < rolls[1] < rolls[2]:
        P +=1

print(f"Probability strictly increasing = {P/N}")