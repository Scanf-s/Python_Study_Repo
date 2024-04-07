import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TREASURE_COLOR = (255, 215, 0)  # Gold
PLAYER_COLOR = (30, 144, 255)  # Dodger Blue
INFO_TEXT_COLOR = (255, 255, 255)
CLOSE_DISTANCE_COLOR = (255, 0, 0)

# Game settings
grid_size = 10  # N x N grid
cell_size = screen_width // grid_size  # Size of each cell
font_size = 30
font = pygame.font.SysFont("arial", font_size, True)

# Game variables initialization function
def init_game():
    player_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    treasure_position = player_position
    while treasure_position == player_position:
        treasure_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    move_count = 0
    return player_position, treasure_position, move_count

player_position, treasure_position, move_count = init_game()

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
easy_mode = True
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
                pygame.draw.rect(screen, TREASURE_COLOR, rect)

    distance = calculate_distance(player_position, treasure_position)
    color = CLOSE_DISTANCE_COLOR if distance <= 5 else INFO_TEXT_COLOR
    draw_text(screen, f"움직인 횟수 : {move_count}", (10, 610), font)
    if easy_mode:
        draw_text(screen, f"보물까지의 거리 : {distance}", (10, 640), font, color)

    if player_position == treasure_position:
        draw_text(screen, "보물을 찾았습니다.", (100, 300), font, (0, 255, 0))
        draw_text(screen, "한판 더 하시겠습니까? : R, 아니면 끝내시겠습니까? : Q", (50, 340), font, (255, 255, 0))
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
