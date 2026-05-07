"""
Race to Ace
What is the expected number of cards you need to draw 
from a 52-card deck before you see the first ace?
"""

import numpy as np

class Deck:
    def __init__(self):
        self.cards = np.repeat(np.array(list(range(1, 14))), 4)
        self.rng = np.random.default_rng(45)
        self.rng.shuffle(self.cards)

    def draw_card(self, n=52):
        self.order = self.rng.choice(self.cards, size=n, replace=False)
        return np.argmax(self.order == 1) + 1
    

E = 0
N = 1_000_000
d = Deck()

for _ in range(N):
    E += d.draw_card()

print(f"Expected draws to first Ace = {E/N}")