from src.constants import *
from src.utils import *


# Define the show_ui function to visualize the agent's best path
def show_ui(obstacles, bonus_cells, best_path, start_pos, target_pos):
    state = start_pos  # Set the initial state to the start position
    running = True  # Control variable for the main loop

    index = 0  # Index for the best path
    collected_bonuses = []  # Initialize the collected bonuses list

    # Main loop for the visualization
    while running:
        # Fill the screen with a white background
        screen.fill(white)

        # Draw grid lines on the screen
        for row in range(grid_size[0]):
            for col in range(grid_size[1]):
                draw_cell((row, col), black, size=0.1)

        # Draw the agent at its current position in blue
        draw_cell(state, blue, size=0.7)

        # Draw the target position in green
        draw_cell(target_pos, green, size=0.7)

        # Draw obstacles in red
        for obstacle in obstacles:
            draw_cell(obstacle, red, size=0.7)

        # Draw bonus cells in gold
        for bonus_cell in bonus_cells:
            if bonus_cell not in collected_bonuses:
                draw_cell(bonus_cell, gold, size=0.5)

        # Update the screen with the new drawings
        pygame.display.flip()

        # Flag for progressing through the path
        progress = False

        # Loop until there is input to progress through the path
        while not progress:
            # Check for events (user input)
            for event in pygame.event.get():
                # If the user closes the window
                if event.type == pygame.QUIT:
                    running = False
                    progress = True
                # If the user presses the space key
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Update state with the next position from the best path
                    state = best_path[index]
                    index += 1  # Increment the best path index
                    progress = True  # Set progress flag to true

                    # If the new state contains a bonus cell, add it to collected bonuses
                    if state in bonus_cells:
                        collected_bonuses.append(state)
