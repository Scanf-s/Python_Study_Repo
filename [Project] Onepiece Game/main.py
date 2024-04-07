import sys

import pygame
import class_obj.GameSettings as gs
from module.settings_menu import *


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


if __name__ == "__main__":
    main()
