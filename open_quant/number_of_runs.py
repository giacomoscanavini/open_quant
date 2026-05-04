"""
Number of Runs
Imagine you are given a standard deck of 52 cards 
(half of the cards are red and the other half are black). 
A run is defined as a block of cards that are drawn consecutively 
and all have the same color. As an example, BBRRBBB has 3 runs.

1) Find the expected number of runs in a shuffled deck of cards.
2) Write a program that calculates the expected number of runs in a deck of X cards with Y colors.
"""

import numpy as np

class Deck:
    def __init__(self, nCards, nColors):
        self.cards = list(range(0, nColors)) * int(nCards / nColors)

    def shuffle_deck(self):
        np.random.shuffle(self.cards)

    def count_runs(self):
        runs = 1 + sum([b != a for a,b in zip(self.cards, self.cards[1:])])
        return runs

E = 0
N = 1_000  
nCards = 52
nColors = 2
d = Deck(nCards=nCards, nColors=nColors)
for _ in range(N):
    d.shuffle_deck()
    E += d.count_runs()

print(f"1) Expected number of runs = {E/N}")

E = 0
N = 1_000
nCards = 32
nColors = 4
d = Deck(nCards=nCards, nColors=nColors)
for _ in range(N):
    d.shuffle_deck()
    E += d.count_runs()

print(f"2) Expected number of runs for {nColors} colors and {nCards} cards = {E/N}")

