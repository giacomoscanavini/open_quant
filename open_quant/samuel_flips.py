"""
Samuel Flips
Samuel flips a fair coin until he lands a tails. By playing this game, Samuel receives 
min(64, 2^n) dollars, where n is the number of times he flipped the coin. 
What is Samuel's expected payoff?
"""

import numpy as np

toss = ['H', 'T']
N = 100000
E = 0

for _ in range(N):
    n = 0 
    while 1:
        n +=1
        if np.random.choice(toss) == "T":
            break
        else:
            pass
    
    if n < 6: E += 2**n
    else:     E += 64

print(f"Samuel's expected payoff = {E/N}")