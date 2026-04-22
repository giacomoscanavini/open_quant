"""
Multiple of Six
You roll a fair six-sided and sum the outcomes until you reach a multiple of 6.
What is the expected number of times you expect to roll the die.
"""

import numpy as np

class DiceGame:
    def __init__(self):
        self.d6 = list(range(1, 7))
        self.total = 0
        self.rolls = 0

    def roll_dice(self):
        self.rolls += 1
        self.total += np.random.choice(self.d6)

        if self.total % 6 == 0:
            return self.rolls
        else:
            return self.roll_dice()
        
N = 100000
n = 0

for _ in range(N):
    d = DiceGame()
    n += d.roll_dice()

print(f"Number of rolls needed = {n/N}")