"""
Four of a Kind
What is the probability of drawing 4 of a kind from a standard 5-card hand?
"""

import numpy as np
import random
from itertools import product

class Deck:
    def __init__(self):
        suit = ['H', 'D', 'S', 'C']
        rank = ['A'] + list(map(str, list(range(2, 11)))) + ['J', 'Q', 'K']
        self.deck = list(product(rank, suit))

    def draw_hand(self, n=5):
        self.hand = random.sample(self.deck, k=n)

    def evaluate_hand_four_of_a_kind(self):
        ranks = [x[0] for x in self.hand]
        if 4 in np.unique(ranks, return_counts=True)[1]:
            return True
        else:
            return False

N = 100000
P = 0
d = Deck()

for _ in range(N):
    d.draw_hand()
    if d.evaluate_hand_four_of_a_kind():
        P+=1

print(f"Probability four of a kind = {P/N}")
        
    