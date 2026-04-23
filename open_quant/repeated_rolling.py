"""
Repeated Rolling
Suppose a game has you roll a fair six-sided die repeatedly, 
until you first encounter a number which has previously appeared. 
Let r denote number of times the die was rolled, and P(r) the probability of rolling r times.

Part 1
Calculate P(r=3)
 
Part 2
What is the value of P(1) + ... + P(10) ?

Part 3
What is P(r=5 | iteration of the game has taken at least 3 rolls) ?
"""

import numpy as np

def play_game():
    seen = []
    game = np.random.choice(list(range(1, 7)), size=7, replace=True)

    for x in game:
        if x in seen: 
            return len(seen) + 1
        else:
            seen.append(x)

N = 100000
N3 = 0

stopping_time = {}
stopping_time_at_least_3 = {}
for _ in range(N):
    roll = play_game()
    stopping_time[roll] = stopping_time.get(roll, 0) + 1

    if roll >= 3:
        N3 += 1
        stopping_time_at_least_3[roll] = stopping_time_at_least_3.get(roll, 0) + 1

rolls = stopping_time.keys()
values = stopping_time.values()

zipped = sorted(zip(rolls, values), key=lambda x: x[0])
rolls, values = zip(*zipped)

for roll, val in zip(rolls, values):
    print(f"P(r = {roll}) = {val/N}")


rolls = stopping_time_at_least_3.keys()
values = stopping_time_at_least_3.values()

zipped = sorted(zip(rolls, values), key=lambda x: x[0])
rolls, values = zip(*zipped)

for roll, val in zip(rolls, values):
    print(f"P(r = {roll} | At least 3 rolls) = {val/N3}")