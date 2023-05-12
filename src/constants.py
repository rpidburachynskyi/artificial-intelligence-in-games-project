import random

import numpy as np

from pygame import display

# Define grid parameters
grid_size = (10, 10)
cell_size = 25
screen_size = (cell_size * grid_size[0], cell_size * grid_size[1])

# Create the screen
screen = display.set_mode(screen_size)
display.set_caption('Reinforcement Learning Example')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
gold = (255, 215, 0)

# Define learning parameters
alpha = 0.05
gamma = 0.99
n_episodes_for_each_agent = 5000

# Available actions: up, down, left, right
actions = ['U', 'D', 'L', 'R']
action_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

num_obstacles = 5
num_bonus_cells = 10

# Train the agents in parallel
n_agents = 1
agent_ids = list(range(n_agents))
