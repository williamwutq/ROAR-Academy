import matplotlib.pyplot as plt
import numpy as np

# Create the plot
fig, ax = plt.subplots()
t1 = np.arange(1.0, 2.0, 0.001)
t2 = np.arange(2.0, 3.0, 0.001)
plt.plot(t1, np.where(True, 2 * t1, t1), lw=2, color='blue')
plt.plot(t2, np.where(True, 10 - 3 * t2, t2), lw=2, color='blue')
ax.set_xlim(1, 3)
ax.set_ylim(1, 4)

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('Sample Graph!')

ax.margins(x=0)

plt.show()