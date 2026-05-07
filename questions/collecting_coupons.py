"""
Collecting Coupons
Coupons in cereal boxes are numbered 1 to 5, 
and a set of one of each is required for a prize. 
With one coupon per box, how many boxes on the average are required to make a complete set?
"""

import numpy as np

coupons = list(range(1, 6))

N = 100000
n = 0

for _ in range(N):
    owned = []
    while len(owned) != 5:
        coupon = np.random.choice(coupons, size=1)[0]
        n += 1
        if coupon not in owned: 
            owned.append(coupon)

print(f"Number of coupons opened = {n/N}")

