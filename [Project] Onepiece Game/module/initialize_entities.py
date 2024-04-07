import random


def init_game(grid_size):
    player_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    treasure_position = player_position
    while treasure_position == player_position:
        treasure_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    move_count = 0
    return player_position, treasure_position, move_count