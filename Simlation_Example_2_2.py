from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

def cfl_condition(dx, dy, nu):
    """
    Applies the CFL condition for diffusion to determine the appropriate time step.
    
    Parameters:
    dx, dy (float): Space step in x and y direction
    nu (float): Kinematic viscosity

    Returns:
    float: Time step (dt) satisfying the CFL condition
    """
    # CFL condition for diffusion
    dt = min(dx**2, dy**2) / (4 * nu)
    return dt

# Simulation parameters
nx, ny = 41, 41  # Grid size
nt = 5000  # Number of timesteps
dx = 2 / (nx - 1)  # Distance between grid points in x
dy = 2 / (ny - 1)  # Distance between grid points in y
nu = 0.15  # Kinematic viscosity
dt = cfl_condition(dx, dy, nu)

# Initial conditions: stationary fluid
U = np.zeros((ny, nx))

# Boundary conditions
Ux0 = 0
Ux1 = 0
Uy0 = 100
Uy1 = 100
U[0, :] = Uy0  # Top boundary (inlet)
U[-1, :] = Uy1  # Bottom boundary (outlet)

# === Animation === #

# Setup the plot
fig, ax = plt.subplots(figsize=(10, 6))
contour = ax.contourf(np.linspace(0, 2, nx), np.linspace(0, 2, ny), U, alpha=0.7, cmap="viridis")
plt.colorbar(contour, ax=ax, label='Velocity')
ax.set_xlim(0, nt)

def init():
    global U
    U = np.zeros((nx, ny))
    U[0, :] = 0  # Top boundary (inlet)
    U[-1, :] = 100  # Bottom boundary (outlet)
    return contour.collections


def animate(step):
    global U
    Un = U.copy()
    # Update the velocity field based on the finite difference method
    U[1:-1, 1:-1] = (Un[1:-1, 1:-1] +
                    nu * dt / dx**2 * (Un[1:-1, 2:] - 2 * Un[1:-1, 1:-1] + Un[1:-1, 0:-2]) +
                    nu * dt / dy**2 * (Un[2:, 1:-1] - 2 * Un[1:-1, 1:-1] + Un[0:-2, 1:-1]))
    
    # Boundary conditions: flow between two parallel lines
    U[:, 0] = 0  # Left boundary
    U[:, -1] = 0  # Right boundary
    U[0, :] = 100  # Top boundary (inlet)
    U[-1, :] = 100  # Bottom boundary (outlet)

    ax.clear()
    contour = ax.contourf(np.linspace(0, 2, nx), np.linspace(0, 2, ny), U, alpha=0.7, cmap="viridis")
    return contour.collections


# Create the animation
ani = FuncAnimation(
    fig, animate, frames=nt, init_func=init, blit=True, interval=100
)

plt.show()