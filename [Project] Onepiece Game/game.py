import pygame
import random

# 게임 설정
screen_width = 600
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

print("게임맵 크기를 입력해주세요 (10 ~ 30) : ")
while True:
    grid_size = int(input())  # grid 생성
    if grid_size <= 30 and grid_size >= 10:
        break
    else:
        print("10 ~ 30 사이의 숫자 입력하세요")

cell_size = screen_width // grid_size

print("난이도 설정 (e : EASY, h : HARD): ")
while True:
    difficulty = input().lower()
    if difficulty == 'e' or difficulty == 'h':
        break
    else:
        print("e 또는 h를 입력하세요")


# Initialize Pygame
pygame.init()

# Color Definition
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TREASURE_COLOR = (255, 215, 0)  # Gold
PLAYER_COLOR = (30, 144, 255)  # Dodger Blue
RED = (255, 0, 0)


# init
def init_game():
    player_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    treasure_position = player_position
    while treasure_position == player_position:
        treasure_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    move_count = 0
    return player_position, treasure_position, move_count


player_position, treasure_position, move_count = init_game()

# Font 설정
pygame.font.init()
font_size = 40
font = pygame.font.SysFont("arial", font_size, True)

# Image 설정
# https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame
background_image = pygame.image.load("images/Background.jpg")
background = pygame.transform.scale(background_image, (screen_width, screen_height))
background_rect = background.get_rect()

player_image = pygame.image.load("images/Luffy.png")
player = pygame.transform.scale(player_image, (cell_size, cell_size))

# Text 표시 함수
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
def draw_text(screen, text, position, font, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)


# Keyboard arrow 처리
# https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
def handle_input(player_pos, move_count):
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


# 사용자 ~ 보물 거리 계산
def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


# Main game loop
running = True
game_over = False

while running:
    screen.blit(background, background_rect)
    running, player_position, move_count = handle_input(player_position, move_count)

    for x in range(grid_size):
        for y in range(grid_size):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, WHITE, rect, 1)
            if (x, y) == player_position:
                screen.blit(player, (player_position[0] * cell_size, player_position[1] * cell_size))
                # pygame.draw.rect(screen, PLAYER_COLOR, rect)
            elif (x, y) == treasure_position:
                # pygame.draw.rect(screen, TREASURE_COLOR, rect)
                pass  # 보물 숨김

    distance = calculate_distance(player_position, treasure_position)
    color = RED if distance <= 5 else BLACK

    draw_text(screen, f"Move count : {move_count}", (10, 610), font, color)
    # Easy 난이도인 경우 추가 힌트 제공
    if difficulty == 'e':
        draw_text(screen, f"Distance : {distance}", (10, 650), font, color)

    if move_count >= grid_size * 2:
        draw_text(screen, "You arrested by Navy", (100, 300), font, (0, 255, 0))
        draw_text(screen, "Retry? : R, Quit? : Q", (150, 350), font, (255, 255, 0))
        game_over = True

    if player_position == treasure_position and move_count < grid_size * 2:
        draw_text(screen, "You found Onepiece!!!!", (100, 300), font, (0, 255, 0))
        draw_text(screen, "Retry? : R, Quit? : Q", (150, 350), font, (255, 255, 0))
        game_over = True

    pygame.display.flip()

    if game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart
                    player_position, treasure_position, move_count = init_game()
                    game_over = False
                elif event.key == pygame.K_q:  # Quit
                    running = False

pygame.quit()
