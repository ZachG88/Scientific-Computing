import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5, 5 + 0.5, 0.5)
y = x
plt.plot(x,y,color="black")
plt.plot(x,y,color="blue",marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
