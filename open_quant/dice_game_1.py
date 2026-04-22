"""
Dice Game 1
Two players take turns rolling two six-sided dice. 
Player A goes first, followed by player B. 
If player A rolls a sum of 6, they win. 
If player B rolls a sum of 7, they win. 
If neither rolls their desired value, the game continues until someone wins. 
What is the probability that player A wins?
"""

import numpy as np

class DiceGame:
    def __init__(self):
        self.d6 = list(range(1, 7))
        self.turn = 'A'
        #self.rolls_history = []
        
    def play_game(self):
        rolls = np.random.choice(self.d6, size=2, replace=True)
        #self.rolls_history.append(np.sum(rolls))

        if self.turn == 'A':
            if np.sum(rolls) == 6: 
                #print(self.rolls_history)
                return self.turn
            else:
                self.turn = 'B'
                return self.play_game()
        
        else:
            if np.sum(rolls) == 7: 
                #print(self.rolls_history)
                return self.turn
            else:
                self.turn = 'A'
                return self.play_game()
            
        
N = 100000
Pa = 0
Pb = 0

for _ in range(N):
    d = DiceGame()
    result = d.play_game()
    if result == 'A':
        Pa += 1
    elif result == 'B':
        Pb += 1

print(f"A wins with P = {Pa/N}")
print(f"B wins with P = {Pb/N}")