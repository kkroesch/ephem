import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)
p = plt.plot(x, y)
plt.savefig('sinx.svg')
#plt.show()
