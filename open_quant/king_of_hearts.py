"""
King of Hearts
You take a standard shuffled deck of cards and keep flipping cards over until the first ace appears, which is card #14.
What's the probability the next card is the king of hearts
"""

import numpy as np
from itertools import product


class Deck:
    def __init__(self, rng):
        self.ranks = list(range(1, 14))
        self.suits = ['H', 'C', 'D', 'S']
        self.cards = list(product(self.ranks, self.suits))

        self.rng = rng
        self.make_deck_valid()

    def make_deck_valid(self):
        self.valid = False

        while not self.valid:
            self.rng.shuffle(self.cards)
            ranks = [card[0] for card in self.cards]

            if all(r != 1 for r in ranks[:13]) and ranks[13] == 1:
                self.valid = True


N = 100000
P = 0

rng = np.random.default_rng(5)

for _ in range(N):
    d = Deck(rng)

    # cards[13] is 14th card
    # cards[14] is 15th card
    if d.cards[14] == (13, 'H'):
        P += 1

print(f"Probability Ace at 14th and KH next = {P / N}")        