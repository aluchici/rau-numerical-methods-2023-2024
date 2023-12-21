import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation


# Define the agent types
class Agent:
    def __init__(self, type, sensitivity, frequency):
        self.type = type
        self.sensitivity = sensitivity
        self.frequency = frequency
        self.purchase_history = []

    def decide_to_buy(self, price):
        # The decision to buy is based on sensitivity to price and a random factor based on frequency
        return random.random() < self.frequency / price**self.sensitivity


# Initialize agents
num_agents = 50
agents = [
    Agent("Impulsive", sensitivity=0.5, frequency=0.9),
    Agent("Neutral", sensitivity=1.0, frequency=0.6),
    Agent("Conservative", sensitivity=1.5, frequency=0.3),
] * (num_agents // 3)

# Market simulation parameters
num_steps = 100
base_price = 10
price_fluctuation = 2.5
total_purchases = []

# Setup the plot
fig, ax = plt.subplots(figsize=(10, 6))
(line,) = ax.plot([], [], lw=2)
ax.set_xlim(0, num_steps)
ax.set_ylim(0, num_agents)
ax.set_xlabel("Time Step")
ax.set_ylabel("Number of Purchases")
ax.set_title("Market Simulation with Impulsive, Neutral, and Conservative Agents")


def init():
    line.set_data([], [])
    return (line,)


def animate(step):
    current_price = base_price + random.uniform(-price_fluctuation, price_fluctuation)
    purchases = sum(agent.decide_to_buy(current_price) for agent in agents)
    total_purchases.append(purchases)

    line.set_data(range(step + 1), total_purchases)
    return (line,)


# Create the animation
ani = FuncAnimation(
    fig, animate, frames=num_steps, init_func=init, blit=True, interval=100
)

plt.show()
