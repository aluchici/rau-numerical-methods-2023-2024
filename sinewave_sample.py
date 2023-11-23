import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], lw=3)

# Initialization function for the animation
def init():
    line.set_data([], [])
    return line,

# The animation function, which updates the plot
def animate(i):
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x + i * 0.1) # Sine wave that changes over time
    line.set_data(x, y)
    return line,

# Creating the animation
ani = FuncAnimation(fig, animate, init_func=init, frames=1000, interval=10)

# Display the animation
plt.show()
