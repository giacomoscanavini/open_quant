"""
Median Probability
Given three random variables independently and identically distributed 
from a uniform distribution of 0 to 4, 
what is the probability that the median of them is greater than 3?
"""

import numpy as np
import matplotlib.pyplot as plt

N = 100000
P = 0

dist = []

for _ in range(N):
    values = np.random.uniform(0, 4, size=3)
    median = np.median(values)
    dist.append(median)

    if median > 3: 
        P +=1

print(f"Probability median(x1, x2, x3) > 3 = {P/N}")

fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.hist(dist, bins=50, range=(0,4), density=True, label=f'f(median(x1, x2, x3))')
ax.axvline(3, lw=1, ls=':', color='red', alpha=0.5)

histogram = np.histogram(dist, bins=50, range=(0,4), density=True)
area_to_integrate = [y for y,x in zip(histogram[0], histogram[1][1:]) if x > 3]
p_med_3 = np.trapezoid(y=area_to_integrate, x=[val for val in histogram[1][1:] if val > 3])

ax.set_xlim(0, 4)
ax.legend(title=f"P(median(x1, x2, x3) > 3) = {round(p_med_3, 3)}")
plt.show()
