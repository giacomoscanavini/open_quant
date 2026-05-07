"""
Straight Shooter
If we define a straight to be 5 cards with consecutive rank, not all sharing the same suit
what is the probability of being dealt a straight in a 5-card poker hand from a standard deck of cards?
"""

import numpy as np
from itertools import product
import random

class Deck:
    def __init__(self):
        ranks = list(range(1, 14))
        suits = ['H', 'D', 'C', 'S']
        self.deck = list(product(ranks, suits))

    def give_hand(self, n = 5):
        self.hand = random.sample(self.deck, k=n)

    def evaluate_straight(self, n = 5):
        ranks = [x[0] for x in self.hand]
        suits = [x[1] for x in self.hand]
        
        ranks = np.unique(ranks) # already ordered
        suits = np.unique(suits) # already ordered

        if len(ranks) != n: 
            # Duplicate ranks
            return False
        else:
            if len(suits) == 1:
                # Same suits 
                return False
            else:
                diff = [b-a for a,b in zip(ranks, ranks[1:])]
                if sum(diff) != 4: 
                    return False
                else: 
                    return True
                
N = 100000
P = 0
d = Deck()

for _ in range(N):
    d.give_hand()
    if d.evaluate_straight():
        P += 1

print(f"Probability of straight = {P/N}")

