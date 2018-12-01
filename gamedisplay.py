import pygame
class init:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((500,500))
        self.size = 600
        self.clock = pygame.time.Clock()
