"""
Variable Swap
Consider a simple univariate linear regression. We have the following X and Y values
We regress Y onto X and obtain some β. 
Now, we regress X onto Y 
Without doing any calculation, how does β change?
"""

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


N = 100
x = np.linspace(-10, 15, N)
y = np.random.normal(loc=0, scale=10, size=100) + np.random.normal(loc=2, scale=0.1, size=N) * x

fig, ax = plt.subplots(1, 2, figsize=(10,4))

X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
print(model.summary())
y_pred = model.predict(X)
y_pred = y_pred.flatten()

ax[0].scatter(x, y, color='black')
ax[0].plot(x, y_pred, color='red')
ax[0].set_xlabel('X', loc='right')
ax[0].set_ylabel('Y')

Y = sm.add_constant(y)
model = sm.OLS(x, Y).fit()
print(model.summary())
x_pred = model.predict(Y)
x_pred = x_pred.flatten()

ax[1].scatter(y, x, color='black')
ax[1].plot(y, x_pred, color='red')
ax[1].set_xlabel('Y', loc='right')
ax[1].set_ylabel('X')

plt.show()