import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10,10,1024)
y = np.sin(x)
plt.plot(x, y)
plt.savefig("my_fig.png")


