"""
The Dealer's Deck
You walk into a casino and play a game with the dealer. 
You and the dealer are each dealt a card from a fair, 
shuffled deck of 52 cards. If you have a strictly larger number than 
the dealer you will win, otherwise you will lose. 
What is the probability that you win?
"""

import numpy as np

N = 100000
P = 0
cards = list(range(1, 14)) * 4


for _ in range(N):
    hands = np.random.choice(cards, size=2, replace=False)
    if hands[0] > hands[1]:
        P += 1

print(f"Probability of higher card: {P/N}")