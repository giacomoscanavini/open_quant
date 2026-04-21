"""
Sequential Pairs
Sam has a standard 52 deck of cards. He pulls two cards and they happen to share the same rank. 
What is the probability that the next two cards he draws also share the same rank?
"""

import numpy as np
from itertools import product
import random

class Deck:
    def __init__(self):
        ranks = list(range(1, 14))
        suits = ['H', 'D', 'C', 'S']
        self.deck = list(product(ranks, suits))

        # Remove form deck 2 cards sharing same rank
        self.deck = self.deck[:-2]

    def give_hand(self, n=2):
        self.hand = random.sample(self.deck, k=n)

    def evaluate_hand(self):
        ranks = [x[0] for x in self.hand]
        if len(np.unique(ranks)) == 1: 
            return True
        else:
            return False

N = 100000
P = 0
d = Deck()

for _ in range(N):
    d.give_hand()
    if d.evaluate_hand():
        P +=1

print(f"Probability of 2 with same rank given removed 2 with same rank = {P/N}")


    