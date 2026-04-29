"""
Brownian motion
What is the probability of Brownian Motion hitting -2 before 1?
"""

import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(mu, t, steps=100):
    dt = t/N
    dW = np.concatenate(([0], np.random.normal(loc=mu, scale=np.sqrt(dt), size=N)))
    W = np.cumsum(dW)
    t = np.linspace(0, t, N+1)

    return t, W

N = 1000
valid = N
P = 0
steps = 100
time = 5

fig, ax = plt.subplots(1, 1, figsize=(8, 5))

for _ in range(N):
    t, W = brownian_motion(mu=0, t=time, steps=steps)

    for val in W:
        if val > 1:
            ax.plot(t, W, alpha=0.15, color='red')
            break

        elif val < -2:
            P += 1
            ax.plot(t, W, alpha=0.15, color='blue')
            break
    else:
        valid -= 1

ax.axhline(-2, lw=1, ls=':', color='black', alpha=0.5)
ax.axhline(1, lw=1, ls=':', color='black', alpha=0.5)
ax.set_xlim(0, time)
ax.set_ylim(-4, 4)
ax.set_xlabel("Time")
ax.set_ylabel("W(t)")
plt.show()

print(f"P(W(t) < -2 before W(t) > 1) = {P/valid}")