# Text 표시 함수
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
def draw_text(screen, text, position, font, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)