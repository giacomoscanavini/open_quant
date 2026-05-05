"""
Place or Take
You are playing a one-player game with two opaque boxes. 
At each turn, you can choose to either "place" or "take". 
"Place" places $1 from a third party into one box randomly. 
"Take" empties out one box randomly and that money is yours. 
This game consists of 100 turns where you must either place or take. 
Assuming optimal play, what is the expected payoff of this game?
"""

import numpy as np
import scipy

func = lambda N: - N * (1 - (1/2)**(100 - N))

best_N = scipy.optimize.minimize(func, 0, method='BFGS')

print(f"Best value for N is {round(best_N['x'][0])}")

