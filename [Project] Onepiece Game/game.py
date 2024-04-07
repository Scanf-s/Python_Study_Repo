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


#########################################################################################################################################################
# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TREASURE_COLOR = (255, 215, 0)  # Gold
PLAYER_COLOR = (30, 144, 255)  # Dodger Blue
INFO_TEXT_COLOR = (255, 255, 255)
CLOSE_DISTANCE_COLOR = (255, 0, 0)

# Game variables initialization function
def init_game():
    player_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    treasure_position = player_position
    while treasure_position == player_position:
        treasure_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    move_count = 0
    return player_position, treasure_position, move_count

player_position, treasure_position, move_count = init_game()
font_size = 30
font = pygame.font.SysFont("arial", font_size, True)

# Text display function
def draw_text(screen, text, position, font, color=INFO_TEXT_COLOR):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

# Handle player input
def handle_input(player_pos, move_count):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, player_pos, move_count
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:    # Move North
                player_pos = (player_pos[0], max(0, player_pos[1] - 1))
            elif event.key == pygame.K_DOWN:  # Move South
                player_pos = (player_pos[0], min(grid_size - 1, player_pos[1] + 1))
            elif event.key == pygame.K_LEFT:  # Move West
                player_pos = (max(0, player_pos[0] - 1), player_pos[1])
            elif event.key == pygame.K_RIGHT:  # Move East
                player_pos = (min(grid_size - 1, player_pos[0] + 1), player_pos[1])
            move_count += 1
    return True, player_pos, move_count

# Calculate Manhattan distance
def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Main game loop
running = True
game_over = False

while running:
    screen.fill(BLACK)
    running, player_position, move_count = handle_input(player_position, move_count)
    
    for x in range(grid_size):
        for y in range(grid_size):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, WHITE, rect, 1)
            if (x, y) == player_position:
                pygame.draw.rect(screen, PLAYER_COLOR, rect)
            elif (x, y) == treasure_position:
                # 개발자 테스트 시 아래 주석을 풀고, pass 주석처리 해주세요
                # pygame.draw.rect(screen, TREASURE_COLOR, rect)
                pass # 보물 숨김

    distance = calculate_distance(player_position, treasure_position)
    color = CLOSE_DISTANCE_COLOR if distance <= 5 else INFO_TEXT_COLOR

    draw_text(screen, f"Move count : {move_count}", (10, 610), font, color)
    if difficulty == 'e':
        draw_text(screen, f"Distance : {distance}", (10, 650), font, color)
    
    if move_count >= grid_size * 2:
        draw_text(screen, "You Lose", (100, 300), font, (0, 255, 0))
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
                if event.key == pygame.K_r:  # Restart game
                    player_position, treasure_position, move_count = init_game()
                    game_over = False
                elif event.key == pygame.K_q:  # Quit game
                    running = False

pygame.quit()
