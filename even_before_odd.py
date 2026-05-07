"""
Even Before Odd
Suppose you roll a fair 6-sided die until you've seen all 6 faces. 
What is the probability you won't see an odd numbered face until you 
have seen all even numbered faces?
"""

import numpy as np

P = 0
N = 100000

class Game:
    def __init__(self):
        self.d6 = list(range(1, 7))

    def play(self):
        seen = []

        while 1: 
            roll = np.random.choice(self.d6)
            if roll & 1 == 1: 
                return False
            else:
                if roll not in seen:
                    if len(seen) == 2:
                        return True
                    else:
                        seen.append(roll)
                else: 
                    continue

d = Game()
for _ in range(N):
    if d.play() == True:
        P += 1


print(f"Probability even before odd = {P/N}")