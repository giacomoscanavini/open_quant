"""
Consecutive Heads
You have a fair coin. 
Denote Xi the time to i consecutive H
Compute the expected values of X1, X2, and X3.
"""

import numpy as np

E1, E2, E3 = 0, 0, 0
N = 100_000

for _ in range(N):
    flag1, flag2, flag3 = False, False, False
    nH = 0
    n = 0
    while nH < 3:
        toss = np.random.choice([0, 1])
        n += 1
        if toss == 1:
            nH += 1

            if nH == 1 and flag1 == False: 
                flag1 = True
                E1 += n
            
            if nH == 2 and flag2 == False:
                flag2 = True
                E2 += n
            
            if nH == 3 and flag3 == False:
                flag3 = True
                E3 += n
        
        else:
            nH = 0

print(f"Time to H = {E1/N}")
print(f"Time to HH = {E2/N}")
print(f"Time to HHH = {E3/N}")