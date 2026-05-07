"""
Spherical Coordinate Variance
Randomly chose a coordinate (x, y, z) on the unit sphere
What is the variance of the z-coordinate?
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1_000

coords = np.random.normal(loc=0, scale=1, size=(3, N))
coords = coords / np.linalg.norm(coords, axis=0)
var_z = np.var(coords[2])

lims = [-1.1, 1.1]

fig, ax = plt.subplots(1, 3, figsize=(18, 5))
ax[0].scatter(coords[0], coords[1])
ax[0].set_xlim(lims)
ax[0].set_ylim(lims)
ax[0].set_xlabel('X')
ax[0].set_ylabel('Y')

ax[1].scatter(coords[0], coords[2])
ax[1].set_xlim(lims)
ax[1].set_ylim(lims)
ax[1].set_xlabel('X')
ax[1].set_ylabel('Z')

ax[2].scatter(coords[1], coords[2])
ax[2].set_xlim(lims)
ax[2].set_ylim(lims)
ax[2].set_xlabel('Y')
ax[2].set_ylabel('Z')
plt.show()

print(f"The variance of z is {var_z}")