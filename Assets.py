import pygame
from utils import *
from settings import *

class Shuriken(pygame.sprite.Sprite):
	def __init__(self, last_dir):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image('shuriken.png')
		self.rect = self.image.get_rect()
		self.last_dir = last_dir
		self.sound = load_sound('shuriken.wav')
		self.sound.play()
		self.timer = 0
	
	def update(self):
		if self.timer >= 4:
			shurikens.remove(self)
		else:
			self.timer += 0.1
		
		self.rect.x += 8 * self.last_dir
	
#--------------------------------------------

class End_sign(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("end.png")
		self.rect = self.image.get_rect()
		
		
		
		
		
		
		
            
