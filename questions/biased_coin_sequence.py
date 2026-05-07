"""
Biased Coin Sequence
You are given a coin with probability 2/3 to land on heads and 1/3 to land on tails. 
If you flip this coin until you get a tails immediately followed by heads, 
how many times do you expect to flip the coin?
"""

import numpy as np

E = 0
N = 100_000

for _ in range(N):
    flag = False
    while 1:
        toss = np.random.choice(['H', 'T'], p=[2/3, 1/3])
        E += 1
        if flag == False:
            if toss == 'T': flag = True
        else:
            if toss == 'H': break


print(f'Expected number of tosses for TH = {E/N}')
