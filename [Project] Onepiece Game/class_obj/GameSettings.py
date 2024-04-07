import pygame

class GameSettings:
    def __init__(self, screen_width=800, screen_height=600, difficulty="easy", volume=50):
        self.volume = int(volume)
        self.screen_width = int(screen_width)
        self.screen_height = int(screen_height)
        self.difficulty = difficulty
        self.font = None  # Initialize font as None or set a default non-Pygame font value

    def font_settings(self):
        self.font = pygame.font.SysFont("Arial", 40)

    def set_screen_dimensions(self, width, height):
        self.screen_width = int(width)
        self.screen_height = int(height)

    def get_screen_dimensions(self):
        return self.screen_width, self.screen_height

    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_volume(self, volume):
        self.volume = int(volume)
