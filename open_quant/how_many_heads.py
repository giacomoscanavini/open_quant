"""
How Many Heads
There are three coins in a hat. One with probability 1/3, one with 2/3 and one with 1 of getting heads
I take one out and flip it twice landing on heads both times. 
If I flip the coin twelve more times, how many heads do you expect among these flips?
"""

import numpy as np

E = 0
N = 100_000
valid = 0

for _ in range(N):
    coin = np.random.choice(['A', 'B', 'C'])

    if coin == 'A':
        p = [1/3, 2/3]
    elif coin == 'B':
        p = [2/3, 1/3]
    else:
        p = [1, 0]

    tosses = np.random.choice([1, 0], size=14, replace=True, p=p)

    if tosses[0] == 1 and tosses[1] == 1:
        E += np.sum(tosses[2:])
        valid += 1
    else:
        continue

print(f'Expected H in 12 tosses = {E/valid}')




