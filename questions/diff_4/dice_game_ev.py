"""
Dice Game EV
1) You are playing a game where two players each throw two dice. 
If any one die matches the other you win a dollar. 
If there is no match you lose a dollar. 
Would you play this game?

2) You are playing a game where you roll one dice. 
If the value of the dice roll is even you will get 2 times the 
value of the roll in dollars. If the value of the dice roll is 
odd you will get just the value of the dice roll. 
You are also given the chance to reroll the dice once. 
How much money do you expect to make by playing this game?
"""

import numpy as np

d6 = list(range(1, 7))


N = 100000
n = 0

for _ in range(N):
    rolls = np.random.choice(d6, size=4, replace=True)
    rolls = set(rolls)
    if len(rolls) < 4: 
        n += 1
    else:
        n -= 1

print(f"1) Expected win per round = {n/N}")



N = 100000
n = 0

for _ in range(N):
    d1, d2 = np.random.choice(d6, size=2, replace=True)
    if d1 == 4 or d1 == 6: 
        n += d1 * 2
    else:
        if d2 in [2, 4, 6]:
            n += d2*2
        else:
            n += d2

print(f"2) Expected win = {n/N}")