"""
Sequential Six
On average, how many times must a 6-sided die be 
rolled until a 6 turns up twice in a row?
"""

import numpy as np

n = 0
N = 10000

d6 = list(range(1, 7))


for _ in range(N):
    last = 0
    while 1:
        roll = np.random.choice(d6)
        n += 1
        if last == 6 and roll == 6:
            break
        else:
            last = roll
    
print(f"Expected rolls for 6-6 = {n/N}")