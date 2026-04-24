"""
Semi-Working Gum Machine
You and two other friends get gum from a semi-functioning gum machine. 
This machine will pop out a stick of gum with a length from the interval [0,3] independently and uniformly. 
Of the 3 sticks, you will receive the shortest one. 
What is the probability the length of your gum stick is between 1 and 2?
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000000
P = 0
dist = []

for _ in range(N):
    values = np.random.uniform(0, 3, size=3)
    minimum = np.min(values)
    dist.append(minimum)

    if 1 < minimum < 2:
        P += 1

print(f"Probability 1 < min(x1, x2, x3) < 2 = {P/N}")

fig, ax = plt.subplots(1, 1, figsize=(8,5))
ax.hist(dist, bins=50, range=(0,3), density=True, label=f'f(min(x1, x2, x3))')
ax.axvline(1, lw=1, ls=':', color='red', alpha=0.5)
ax.axvline(2, lw=1, ls=':', color='red', alpha=0.5)

histogram = np.histogram(dist, bins=50, range=(0,3), density=True)
area_to_integrate = [y for y,x in zip(histogram[0], histogram[1][1:]) if 1 < x < 2]
p_min_1_2 = np.trapezoid(y=area_to_integrate, x=[val for val in histogram[1][1:] if 1 < val < 2])

ax.set_xlim(0, 3)
ax.legend(title=f"P(1 < min(x1, x2, x3) < 2) = {round(p_min_1_2, 3)}")
plt.show()
