import multiprocessing

from src.constants import *
from src.utils import *
from src.ui import show_ui
from src.train import train


def full_train(example_name):
    start_pos = (0, 0)
    target_pos = (grid_size[0] - 1, grid_size[1] - 1)

    obstacles = obstacle_positions(num_obstacles, start_pos, target_pos)
    bonus_cells = bonus_positions(num_bonus_cells, start_pos, target_pos, obstacles)

    best_path, q_table = train(
        obstacles=obstacles,
        bonus_cells=bonus_cells,
        start_pos=start_pos,
        target_pos=target_pos
    )


    save_data_to_json(
        q_table,
        start_pos=start_pos,
        target_pos=target_pos,
        obstacles=obstacles,
        bonus_cells=bonus_cells,
        best_path=best_path,
        grid_size=grid_size,
        example_name=example_name
    )

    return start_pos, target_pos, obstacles, bonus_cells, best_path, q_table


if __name__ == '__main__':
    multiprocessing.freeze_support()

    # comment to either train or load data from json

    # train
    # start_pos, target_pos, obstacles, bonus_cells, best_path, q_table = full_train(
    #     'big-field'
    # )

    # load data from json
    q_table, start_pos, target_pos, obstacles, bonus_cells, grid_size, best_path = load_data_from_json(
        'big-field'
    )

    pygame.init()

    show_ui(
        obstacles=obstacles,
        bonus_cells=bonus_cells,
        best_path=best_path,
        grid_size=grid_size,
        start_pos=start_pos,
        target_pos=target_pos
    )

    # Quit Pygame
    pygame.quit()


