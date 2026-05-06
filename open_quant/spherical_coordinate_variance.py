"""
Spherical Coordinate Variance
Randomly chose a coordinate (x, y, z) on the unit sphere
What is the variance of the z-coordinate?
"""

import numpy as np

N = 100_000

coords = np.random.normal(loc=0, scale=1, size=(3, N))
coords = coords / np.linalg.norm(coords, axis=0)
var_z = np.var(coords[2])

print(f"The variance of z is {var_z}")