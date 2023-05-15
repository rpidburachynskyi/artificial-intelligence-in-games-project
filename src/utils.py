# Import required libraries
import random
import pygame
import numpy as np
import json

# Import constants from the constants module
from src.constants import actions, action_map, grid_size, cell_size


# Function to randomly generate obstacle positions
def obstacle_positions(num_obstacles, start_pos, target_pos):
    positions = []  # Create an empty list to store obstacle positions

    # Keep generating obstacles until desired number is reached
    while len(positions) < num_obstacles:
        # Randomly generate a row and column position within the grid
        row, col = random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1)

        # Create a tuple with the row and column position
        new_pos = (row, col)

        # Add the new position to the list if it's not already there, and it's not the start or target position
        if new_pos not in positions and new_pos != start_pos and new_pos != target_pos:
            positions.append(new_pos)

    return positions  # Return the final list of obstacle positions


# Function to randomly generate bonus cell positions
def bonus_positions(num_bonus_cells, start, target, obstacles):
    positions = []  # Create an empty list to store bonus cell positions
    # Keep generating bonus cells until desired number is reached
    while len(positions) < num_bonus_cells:
        # Randomly generate a row and column position within the grid
        row, col = random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1)

        # Create a tuple with the row and column position
        new_pos = (row, col)

        # Add the new position to the list if it's not already there, it's not the start or target position,
        # and it's not an obstacle
        if new_pos not in positions and new_pos != start and new_pos != target and new_pos not in obstacles:
            positions.append(new_pos)

    return positions  # Return the final list of bonus cell positions


# Function to get the next state after an action is taken
def get_next_state(current_state, action, obstacles, collected_bonuses):
    # Calculate the next position by applying the action to the current state
    next_pos = (current_state[0] + action_map[action][0], current_state[1] + action_map[action][1])

    # Clip the next position between grid limits to prevent going out of bounds
    next_state = tuple(np.clip(next_pos, 0, grid_size[0] - 1))

    # Add the collected bonuses to the next_state tuple
    next_state = next_state + (collected_bonuses,)

    # Return next state if not an obstacle, otherwise return current state (i.e., agent doesn't move)
    return next_state if next_state not in obstacles else current_state


# Function to choose the next action based on Q-table values or random choice (epsilon-greedy approach)
def choose_action(state, q_table, epsilon):
    # Make a random move with probability epsilon
    if random.random() < epsilon:
        return random.choice(actions)
    else:
        # Otherwise, select the action with the highest Q-value for the given state
        return actions[np.argmax(q_table[state])]


# Function to draw a rectangle within the specified cell
def draw_cell(screen, pos, color, size=0.9):
    # Calculate the x and y coordinates (top left corner) of the rectangle
    x = pos[1] * cell_size + (cell_size * (1 - size)) // 2
    y = pos[0] * cell_size + (cell_size * (1 - size)) // 2

    # Calculate the width and height of the rectangle based on given size
    width = cell_size * size
    height = cell_size * size

    # Draw the rectangle on the screen with the given color and dimensions
    pygame.draw.rect(screen, color, (x, y, width, height))


def save_data_to_json(
        q_table,
        start_pos,
        target_pos,
        obstacles,
        bonus_cells,
        grid_size,
        best_path,
        example_name
):
    file_name = f'examples/{example_name}.json'

    data = {
        'q_table': q_table.tolist(),
        'obstacles': list(obstacles),
        'best_path': [(int(t[0]), int(t[1])) for t in best_path],
        'bonus_cells': list(bonus_cells),
        'grid_size': list(grid_size),
        'start_pos': list(start_pos),
        'target_pos': list(target_pos)
    }

    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)


def load_data_from_json(example_name):
    file_name = f'examples/{example_name}.json'

    with open(file_name, 'r') as f:
        data = json.load(f)

    return (
        np.array(data['q_table']),
        tuple(data['start_pos']),
        tuple(data['target_pos']),
        set(tuple(t) for t in data['obstacles']),
        set(tuple(t) for t in data['bonus_cells']),
        tuple(data['grid_size']),
        tuple(tuple(t) for t in data['best_path'])
    )
