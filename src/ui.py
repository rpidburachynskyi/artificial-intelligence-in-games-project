from pygame import display

from src.constants import *
from src.utils import *


# Define the show_ui function to visualize the agent's best path
def show_ui(obstacles, bonus_cells, best_path, grid_size, start_pos, target_pos):
    screen_size = (cell_size * grid_size[0], cell_size * grid_size[1])

    # Create the screen
    screen = display.set_mode(screen_size)
    display.set_caption('Reinforcement Learning Example')

    state = start_pos  # Set the initial state to the start position
    running = True  # Control variable for the main loop

    index = 0  # Index for the best path
    collected_bonuses = set()  # Initialize the collected bonuses list

    pressed_progress = False

    # Main loop for the visualization
    while running and state != target_pos or len(collected_bonuses) != len(bonus_cells):
        # Fill the screen with a white background
        screen.fill(white)

        # Draw grid lines on the screen
        for row in range(grid_size[0]):
            for col in range(grid_size[1]):
                draw_cell(screen, (row, col), black, size=0.1)

        # Draw the agent at its current position in blue
        draw_cell(screen, state, blue, size=0.7)

        # Draw the target position in green
        draw_cell(screen, target_pos, green, size=0.7)

        # Draw obstacles in red
        for obstacle in obstacles:
            draw_cell(screen, obstacle, red, size=0.7)

        # Draw bonus cells in gold
        for bonus_cell in bonus_cells:
            if bonus_cell not in collected_bonuses:
                draw_cell(screen, bonus_cell, gold, size=0.5)

        # Update the screen with the new drawings
        pygame.display.flip()

        # Loop until there is input to progress through the path
        # Check for events (user input)
        for event in pygame.event.get():
            # If the user closes the window
            if event.type == pygame.QUIT:
                running = False
            # If the user presses the space key
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pressed_progress = not pressed_progress

        if pressed_progress:
            # Update state with the next position from the best path
            state = best_path[index]
            index += 1  # Increment the best path index

            # If the new state contains a bonus cell, add it to collected bonuses
            if state in bonus_cells:
                collected_bonuses.add(state)

        pygame.time.wait(50)


