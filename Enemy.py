import pygame
from utils import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('snake.png')
        self.rect = self.image.get_rect()
        