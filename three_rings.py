"""
Three Rings

1) You are shooting arrows at a target with three rings: there is a circle 
with a 4 inch radius, a ring around it with an 8 inch radius, 
and a ring around that with a 12 inch radius. 
Each arrow hits the target somewhere uniformly at random.
Wha's the probability that you land exactly one arrow in each of the three rings?

2) Now you shoot 3n arrows. Derive an expression that represents the probability that 
you land exactly n arrows in each of the 3 rings?
"""

import numpy as np

N = 1_000_000
P = 0

for _ in range(N):
    n = 12
    rings = [0, 0, 0]

    for i in range(n):
        area = np.random.uniform(0, 144)
        
        if area < 16:
            rings[0] += 1
        elif 16 < area < 64:
            rings[1] += 1
        else:
            rings[2] += 1

    if np.all(np.array(rings) == int(12/3)):
        P += 1

print(f"Probability n arrows per ring = {P/N}")