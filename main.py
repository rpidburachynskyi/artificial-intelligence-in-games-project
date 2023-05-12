import multiprocessing

from src.constants import *
from src.utils import *
from src.ui import show_ui
from src.train import train


if __name__ == '__main__':
    multiprocessing.freeze_support()

    start_pos = (0, 0)
    target_pos = (grid_size[0] - 1, grid_size[1] - 1)

    obstacles = obstacle_positions(num_obstacles, start_pos, target_pos)
    bonus_cells = bonus_positions(num_bonus_cells, start_pos, target_pos, obstacles)

    pygame.init()

    best_path = train(
        obstacles=obstacles,
        bonus_cells=bonus_cells,
        start_pos=start_pos,
        target_pos=target_pos
    )

    show_ui(
        obstacles=obstacles,
        bonus_cells=bonus_cells,
        best_path=best_path,
        start_pos=start_pos,
        target_pos=target_pos
    )

    # Quit Pygame
    pygame.quit()


