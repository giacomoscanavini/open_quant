"""
Safe Codes
An electronic safe has a three digit code. You are given two hints regarding the code to the safe:
- None of the digits are zero
- The sum of the digits does not exceed ten
How many possible three digit entries satisfy these two requirements?
"""

from itertools import product

codes = list(product(range(1, 11), range(1, 11), range(1, 11)))
codes = [code for code in codes if sum(code) <= 10]

codes = [(x,y,z) for x in range(1, 11) for y in range(1, 11) for z in range(1, 11) if x+y+z <= 10]

print(f"Valid codes = {len(codes)}")
