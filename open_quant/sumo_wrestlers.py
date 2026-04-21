"""
Sumo Wrestlers
Two Sumo wrestlers (A and B) have one wrestling match each day for N days. 
Let Xi denote the outcome of a wrestling match on day i for A 
Let Xn denote the fraction of matches that A won.
Assume that each match is independent of the other matches and let p denote 
the probability that sumo A wins the match. If p = 0.63 and σ = 0.025
how many matches must the sumo wrestlers have in order for 
P( 0.57 ≤ Xn ≤ 0.69 ) > 0.88
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000
numbers = [50, 100, 158, 200]

fig, ax = plt.subplots(1, 4, figsize=(20,4))
ax = ax.flatten()

for i,n in enumerate(numbers):
    props = []
    for _ in range(N):
        matches = np.random.choice([1,0], size=n, replace=True, p=[0.63, 0.37])
        props.append(sum(matches)/n)
    
    area_in_between = sum([True for x in props if 0.57 <= x <= 0.69 ]) / N
    ax[i].hist(props, bins=48, range=(0, 1), label=f'Matches (n = {n})', density=True)
    ax[i].axvline(0.57, lw=1, ls=':', color='red', alpha=0.5)
    ax[i].axvline(0.69, lw=1, ls=':', color='red', alpha=0.5)
    ax[i].set_xlabel('Proportion', loc='right')
    ax[i].legend(title=f'P(0.57 < Xn < 0.69) = {round(area_in_between, 3)}')

plt.show()
