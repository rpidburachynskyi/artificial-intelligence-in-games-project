# Define grid parameters
grid_size = (8, 8)
cell_size = 25

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
gold = (255, 215, 0)

# Define learning parameters
alpha = 0.1
gamma = 0.9
n_episodes_for_each_agent = 5000

# Available actions: up, down, left, right
actions = ['U', 'D', 'L', 'R']
action_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

num_obstacles = 12
num_bonus_cells = 8

# Train the agents in parallel
n_agents = 5
agent_ids = list(range(n_agents))
