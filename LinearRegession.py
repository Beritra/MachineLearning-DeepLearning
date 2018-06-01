import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def f(i):
    return np.random.rand() + (i * 1.2 + np.random.rand() / 100)


matplotlib.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
x = 10 * np.random.rand(20)
y = list(map(f, x))

ax.plot(x, y, 'o')
ax.set_title('Using hyphen instead of Unicode minus')
plt.show()
