import pygame
from utils import *
from settings import *

class Smoke(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.images = [ load_image("smoke1.png"), load_image("smoke2.png"),
		load_image("smoke3.png")]
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		self.last_update = 0
		self.current_frame = 0
		self.timer = 0
		self.sound = load_sound("kill.wav")
		self.sound.play()
		
	def update(self):
		animate(self, self.images, 50)
		if self.timer >= 1:
			smokelist.remove(self)
		else:
			self.timer += 0.1
        
        
