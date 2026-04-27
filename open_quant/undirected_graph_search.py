"""
Undirected Graph Search
You are given a complete undirected graph with N ≥ 2 nodes. 
You first select a uniformly random node to go to, and then each step after,
you select to move to any of the nodes (including the one you are presently on) 
in the graph uniformly at random. Find the expected number of turns that are 
performed until you visit all of the nodes with N = 100 and round to the nearest integer.
"""

import numpy as np 

N = 1000
n = 0
sites = 100
all_sites = list(range(1, sites+1))

for _ in range(N):
    seen = []

    while len(seen) < sites:
        new = np.random.choice(all_sites)
        n += 1
        if new not in seen:
            seen.append(new)

print(f"Expected time to visit {sites} sites = {n/N}")
