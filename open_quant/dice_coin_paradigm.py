"""
Dice Coin Paradigm

"""

import numpy as np

P = 0
N = 100000

for _ in range(N):
    n = 0
    while 1: 
        coin = np.random.choice(['T', 'H'])
        n += 1
        if coin == 'H':
            break
    
    rolls = np.random.choice(list(range(1, 7)), size=n, replace=True)
    if 1 in set(rolls):
        P += 1

print(f"Probability to roll 1 in n rolls, where n is time to first coin H = {P/N}")
            