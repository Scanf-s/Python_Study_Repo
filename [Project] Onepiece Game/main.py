import sys

import pygame
import class_obj.GameSettings as gs
from module.settings_menu import *
from module.initialize_entities import *
from module.keyboard_input_handler import *
from module.draw_text import *
from module.calculate_distance import *


def game_start(settings):
    screen_dimensions = settings.get_screen_dimensions()
    start_screen = pygame.display.set_mode(screen_dimensions)
    pygame.display.set_caption("OnePiece Game")

    # 여러 줄로 표시할 메시지
    start_messages = [
        "Welcome to OnePiece Game!",
        "Press SPACE to Start. Or..",
        "Press TAB to Configuration"
    ]

    # 화면 중앙에 메시지를 배치하기 위한 기준 점 계산
    base_y = screen_dimensions[1] / 3 - len(start_messages) * settings.font.get_linesize() / 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                game_settings(settings)
                start_screen = pygame.display.set_mode(settings.get_screen_dimensions())
                pygame.display.update()

        start_screen.fill((255, 255, 255))

        # 여러 줄의 메시지를 화면에 그림
        for i, message in enumerate(start_messages):
            message_object = settings.font.render(message, True, (0, 0, 0))
            message_rect = message_object.get_rect()
            message_rect.centerx = screen_dimensions[0] / 2
            message_rect.y = base_y + i * settings.font.get_linesize()
            start_screen.blit(message_object, message_rect)

        pygame.display.update()


def main():
    pygame.init()

    settings = gs.GameSettings()
    settings.font_settings()
    game_start(settings)

    screen = pygame.display.set_mode(settings.get_screen_dimensions())

    grid_size = 10
    if settings.get_difficulty() == "easy":
        player_position, treasure_position, move_count = init_game(grid_size)
    elif settings.get_difficulty() == "medium":
        grid_size = 20
        player_position, treasure_position, move_count = init_game(grid_size)
    elif settings.get_difficulty() == "hard":
        grid_size = 30
        player_position, treasure_position, move_count = init_game(grid_size)
    else:  # default : easy
        player_position, treasure_position, move_count = init_game(grid_size)
    cell_size = settings.get_screen_dimensions()[1] // grid_size

    # Image 설정
    # https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame
    background_image = pygame.image.load("./images/Background.jpg")
    background = pygame.transform.scale(background_image, settings.get_screen_dimensions())
    background_rect = background.get_rect()

    player_image = pygame.image.load("./images/Luffy.png")
    player = pygame.transform.scale(player_image, (cell_size, cell_size))

    # Main game loop
    running = True
    game_over = False

    while running:
        screen.blit(background, background_rect)
        running, player_position, move_count = handle_input(player_position, move_count, grid_size)

        for x in range(grid_size):
            for y in range(grid_size):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)
                if (x, y) == player_position:
                    screen.blit(player, (player_position[0] * cell_size, player_position[1] * cell_size))
                    # pygame.draw.rect(screen, PLAYER_COLOR, rect)
                elif (x, y) == treasure_position:
                    # pygame.draw.rect(screen, TREASURE_COLOR, rect)
                    pass  # 보물 숨김

        distance = calculate_distance(player_position, treasure_position)
        color = (255, 0, 0) if distance <= 5 else (0, 0, 0)

        x, y = settings.get_screen_dimensions()[0], settings.get_screen_dimensions()[1]
        draw_text(screen, f"Move count : {move_count}", (0, 0), settings.get_font(), color)
        # Easy 난이도인 경우 추가 힌트 제공
        if settings.get_difficulty() == "easy":
            draw_text(screen, f"Distance : {distance}", (0, 50), settings.get_font(), color)

        if move_count >= grid_size * 2:
            draw_text(screen, "You arrested by Navy", (x // 2, y // 2), settings.get_font(), (0, 255, 0))
            draw_text(screen, "Retry? : R, Quit? : Q", (x // 2, y // 2 + 50), settings.get_font(), (255, 255, 0))
            game_over = True

        if player_position == treasure_position and move_count < grid_size * 2:
            draw_text(screen, "You found Onepiece!!!!", (x // 2, y // 2), settings.get_font(), (0, 255, 0))
            draw_text(screen, "Retry? : R, Quit? : Q", (x // 2, y // 2 + 50), settings.get_font(), (255, 255, 0))
            game_over = True

        pygame.display.flip()

        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Restart
                        player_position, treasure_position, move_count = init_game(grid_size)
                        game_over = False
                    elif event.key == pygame.K_q:  # Quit
                        running = False

    pygame.quit()


if __name__ == "__main__":
    main()
