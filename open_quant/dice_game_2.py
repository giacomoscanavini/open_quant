"""
Dice Game 2
We play a game with two tetrahedral dice, red and blue, each with faces labeled 1-4. 
In each turn, you simultaneously roll both dice.
If the blue shows more than the red, you are paid the difference, otherwise paid nothing. 
If the blue and red show the same value, the game is immediately over, otherwise, you take another turn.
What is the fair value of the game?
"""

import numpy as np

E = 0
N = 100_000

roll_die = lambda n: np.random.choice(list(range(1, n+1)))

for _ in range(N):

    while 1:
        roll_blue, roll_red = np.random.choice(list(range(1, 5)), size=2, replace=True)
        
        if roll_blue == roll_red:
            break
            
        elif roll_blue > roll_red:
            E += roll_blue - roll_red

        else:
            pass

print(f"Expected pay = {E/N}")
