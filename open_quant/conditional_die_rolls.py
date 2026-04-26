"""
Conditional Die Rolls
Dan rolls a dice until he gets a 6. 
1) Given that he did not see a 5, what is the expected number of times Dan rolled his die?
2) Given that he saw a 5, what is the expected number of times Dan rolled his die?
3) Given that he saw only even numbers, what is the expected number of times Dan rolled his die?
"""

import numpy as np

P = 0
N = 100000
n = []

for _ in range(N):
    rolls = 0
    while 1: 
        roll = np.random.choice(list(range(1, 7)))
        rolls += 1
        if roll == 5:
            break
        else:
            if roll == 6:
                n.append(rolls)
                break

print(f"1) Expected rolls for a 6 before seeing 5 = {sum(n)/len(n)}")




P = 0
N = 100000
n = []

for _ in range(N):
    rolls = 0
    condition = False
    while 1: 
        roll = np.random.choice(list(range(1, 7)))
        rolls += 1
        if roll == 5:
            condition = True
        elif roll in [1, 2, 3, 4]:
            pass
        else:
            if condition == True:
                n.append(rolls)
                break
            else:
                break

print(f"2) Expected rolls for a 6 after seeing 5 = {sum(n)/len(n)}")




P = 0
N = 100000
n = []

for _ in range(N):
    rolls = 0
    while 1: 
        roll = np.random.choice(list(range(1, 7)))
        rolls += 1
        if roll & 1 == 1 :
            break
        else:
            if roll == 6:
                n.append(rolls)
                break

print(f"3) Expected rolls for a 6 before seeing odd numbers (1,3,5) = {sum(n)/len(n)}")