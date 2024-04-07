import pygame


# Keyboard arrow 처리
# https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
def handle_input(player_pos, move_count, grid_size):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, player_pos, move_count
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # 위로
                player_pos = (player_pos[0], max(0, player_pos[1] - 1))
            elif event.key == pygame.K_DOWN:  # 아래로
                player_pos = (player_pos[0], min(grid_size - 1, player_pos[1] + 1))
            elif event.key == pygame.K_LEFT:  # 왼쪽으로
                player_pos = (max(0, player_pos[0] - 1), player_pos[1])
            elif event.key == pygame.K_RIGHT:  # 오른쪽으로
                player_pos = (min(grid_size - 1, player_pos[0] + 1), player_pos[1])
            move_count += 1
    return True, player_pos, move_count
