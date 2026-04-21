"""
Sitting Birds
Two brown and six red birds are flying around the sky and suddenly all land randomly in line on a telephone wire. 
What is the probability that the two brown birds are side by side?
"""

import numpy as np

P = 0
N = 1000000

birds = ['B'] * 2 + ['R'] * 6

for _ in range(N):
    order = np.random.choice(list(range(1, 9)), size=8, replace=False)
    if abs(order[0] - order[1]) == 1:
        P +=1 

print(f"Probability brown birds next to each other = {P/N}")
