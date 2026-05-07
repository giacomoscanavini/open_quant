"""
Number of Turns
Suppose you have a deck of 20 cards with values ranging from 1 - 10. 
Each card appears in the deck exactly twice. 
You draw 2 cards at a time uniformly at random from the 20 cards. 
If they match in value, you remove them from the deck. 
Otherwise, they are put back into the deck. 
The game finishes once there are no more cards to draw. 
Each drawing of two cards is a turn. 
Find the expected number of turns needed to finish the game.
"""

import numpy as np

class Deck:
    def __init__(self, pairs=10):
        self.pairs = pairs
        self.cards = list(range(1, self.pairs+1)) * 2

    def draw_two(self):
        hand = np.random.choice(self.cards, size=2, replace=False)
        if len(set(hand)) == 1:
            self.pairs -= 1
            self.cards = list(range(1, self.pairs+1)) * 2

    def play_game(self):
        T = 0
        while self.pairs > 0:
            T += 1 
            self.draw_two()

        return T
    
N = 10000
n = 0

for _ in range(N):
    d = Deck()
    n += d.play_game()

print(f"Expected number of turns = {n/N}")