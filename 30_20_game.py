"""
30-20 Game
Two players, Philip and Brandon, have a 30-side and 20-side dice, respectively. 
Each player rolls their dice and the player with the highest roll wins 
(Brandon also wins in the event of a tie). 
The loser of the game pays the winner an amount equivalent to the value of the winner's dice roll.

1) What is the expected value for the payoff of Philip?
2) How much does the expected value of the game change for Philip 
when Brandon can re-roll the dice before Philip's dice is unveiled?
"""

import numpy as np
import matplotlib.pyplot as plt

E_ph = 0
N = 100000

roll_die = lambda sides: np.random.choice(list(range(1, sides+1)))

for _ in range(N):
    ph = roll_die(30)
    br = roll_die(20)

    # No reroll allowed
    if ph > br:
        E_ph += ph
    else:
        E_ph -= br

print(f"1) Expected value for Philip: {E_ph/N}")



# Now let one reroll allowed for Brandon
E_ph_reroll = np.zeros(20)
E_br_reroll = np.zeros(20)
thresholds = list(range(1, 21))

for i,threshold in enumerate(thresholds):
    for _ in range(N):
        ph = roll_die(30)
        br = roll_die(20)

        if br < threshold: 
            br = roll_die(20)

        if ph > br:
            E_ph_reroll[i] += ph
            E_br_reroll[i] -= ph
        else:
            E_ph_reroll[i] -= br
            E_br_reroll[i] += br

fig, ax = plt.subplots(1, 1, figsize=(8,5))
ax.plot(thresholds, E_ph_reroll/N, label='Philip')
ax.plot(thresholds, E_br_reroll/N, label='Brandon')
ax.set_xlim(1, 20)
ax.set_xlabel('Threshold for reroll', loc='right')
ax.set_ylabel('Expected value given threshold')
ax.axhline(8.15, lw=1, ls=':', color='black', alpha=0.5, label='E[Ph] with no reroll')
ax.legend()
plt.show()        

print(f"2) Optimal strategy is Brandon rerolling for values < {thresholds[np.argmin(E_ph_reroll/N)]}")
print(f"Expected value for Philip (with reroll): {E_ph_reroll[np.argmin(E_ph_reroll/N)]/N}")