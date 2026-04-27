"""
Last Marble Standing
Josephine has r red marbles, b blue marbles, and g green marbles in an urn. 
She draws out the marbles one at a time without replacement. 
Find the probability there is at least one green and one blue marble left in 
the urn right after the last red marble is selected. Find the probability when r=10, b=20, g=30.
"""

import numpy as np

N = 100000
P = 0

urn = ['R'] * 10 + ['B'] * 20 + ['G'] * 30
l = len(urn)

for _ in range(N):
    extract = np.random.choice(urn, size=l, replace=False)
    #extract = extract[::-1]

    blue, green = 0, 0
    for ball in extract: 
        if ball == 'G': 
            green += 1
        elif ball == 'B':
            blue += 1
        else:
            break
    
    if blue > 0 and green > 0:
        P += 1

print(f"Probability >1 B and > 1 G when last R = {P/N}")