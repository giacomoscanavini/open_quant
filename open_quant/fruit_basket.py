"""
Fruit Basket
You have a basket with an assortment of fruits. Inside this basket, there are 
10 apples, 20 oranges, and 30 peaches. You take out fruits one by one and at random. 
What is the probability that there will be at least 1 orange 
and 1 peach in the basket after you've taken out all the apples?
"""

import numpy as np

N = 100_000
P = 0

rng = np.random.default_rng(5)

for _ in range(N):
    basket = np.array(['A'] * 10 + ['O'] * 20 + ['P'] * 30)
    basket = rng.choice(basket, size=len(basket), replace=False)

    valid = [False, False]
    for fruit in basket:
        if fruit == 'A':
            break
        elif fruit == 'O':
            valid[0] = True
        else:
            valid[1] = True
    if np.all(np.array(valid) == True):
        P += 1


print(f"Probability of at least 1 orange and 1 peach = {P/N}")

    