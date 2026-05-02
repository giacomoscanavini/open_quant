"""
30-20 Game

"""

import numpy as np

E_ph = 0
E_ph_reroll = 0
N = 1000000

roll_die = lambda sides: np.random.choice(list(range(1, sides+1)))

for _ in range(N):
    ph = roll_die(30)
    br = roll_die(20)

    if ph > br:
        E_ph += ph
    else:
        E_ph -= br

    if br < 12:
        br = roll_die(20)

    if ph > br:
        E_ph_reroll += ph
    else:
        E_ph_reroll -= br


print(f"Expected value for Philip: {E_ph/N}")
print(f"Expected value for Philip (with reroll): {E_ph_reroll/N}")