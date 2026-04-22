"""
Odd Flips
Suppose you flip a fair coin 1,000 times. 
What is the probability you observe an odd number of heads?
"""

import numpy as np

N = 100000
n = 1000
P = 0
p = [1/2, 1/2]

for _ in range(N):
    tosses = np.random.choice([0, 1], size=n, replace=True, p=p)
    if sum(tosses) & 1 == 1:
        P += 1

print(f"Probability 1000 tosses have odd heads (p(H) = {p[1]})= {P/N}")