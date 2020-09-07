#---09
import pygame, os
from Assets import Shuriken
from settings import *
from utils import *

class Player(pygame.sprite.Sprite):
	def __init__(self, block_sprites):
		pygame.sprite.Sprite.__init__(self)
		self.images = [load_image('p.png'), load_image('p2.png')]
		self.right_images = [load_image('pr1.png'), load_image('pr2.png'), load_image('pr3.png')]
		self.left_images = [load_image('pl1.png'), load_image('pl2.png'), load_image('pl3.png')]
		self.attack_imgs = [load_image("at_r.png"), load_image('at_l.png')]
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		self.speed = 0
		self.grav = 0
		self.is_onground = False
		self.block_sprites = block_sprites
		self.accel = 1
		self.deaccel = 1
		self.max_speed = 5
		self.last_update = 0
		self.a = 0
		self.last_dir = 1
		self.s_jump = load_sound('jump.wav')
		self.shuri_timer = 0
		self.is_attacking = False #new
		
	def animate(self, imgs, speed): 
		now = pygame.time.get_ticks()
		
		if now - self.last_update > speed:
			self.last_update = now
			if self.a < len(imgs):
				self.image = imgs[self.a]
				self.a += 1
			else:
				self.a = 0
		
		
	def update(self):
		self.shuri_timer += 0.1
		if self.shuri_timer >= 1:
			self.is_attacking = False
		
		self.grav += 0.8
		motion = [0,0]
		motion[1] += int(self.grav) #gravity
		
		key = pygame.key.get_pressed()
		if key[pygame.K_RIGHT]:
			motion[0] += 1
		if key[pygame.K_LEFT]:
			motion[0] += -1
		if key[pygame.K_ESCAPE]:
			pygame.quit()
		
		self.rect.y += motion[1]
		#---vertical collision check
		col = pygame.sprite.spritecollide(self, self.block_sprites, False)
		for obj in col:
			if motion[1] > 0:
				self.rect.bottom = obj.rect.top
				self.grav = 0
				self.is_onground = True
			if motion[1] < 0:
				self.rect.top = obj.rect.bottom
				self.grav = 0
		#------move left and right
		if motion[0] > 0:
			self.last_dir = 1
			if not self.is_attacking:
				self.animate(self.right_images, 50) #animation
			if self.speed < self.max_speed:
				self.speed += self.accel
			elif self.speed > self.max_speed:
				self.speed = self.max_speed
		elif motion[0] < 0:
			self.last_dir = -1
			self.animate(self.left_images, 50)#animation
			if self.speed > -self.max_speed:
				self.speed += -self.accel
			elif self.speed > self.max_speed:
				self.speed = -self.max_speed
		elif motion[0] == 0:
			#self.animate(self.images, 300) #animation
			if self.last_dir > 0 and self.is_onground and not self.is_attacking:
				self.image = self.right_images[0]
			elif self.last_dir < 0 and self.is_onground and not self.is_attacking:
				self.image = self.left_images[0]
			
			if self.speed > 0:
				self.speed += -self.deaccel
			elif self.speed < 0:
				self.speed += self.deaccel
			else:
				self.speed = 0
		self.rect.x += self.speed 
		#----horizontal collision check
		col = pygame.sprite.spritecollide(self, self.block_sprites, False)
		for obj in col:
			if self.speed > 0:
				self.rect.right = obj.rect.left
			if self.speed < 0:
				self.rect.left = obj.rect.right
		#---jump---
		if key[pygame.K_z] and self.is_onground or key[pygame.K_UP] and self.is_onground:
			self.s_jump.play()
			self.is_onground = False
			self.grav = -15
			
		#---shoot shuriken
		if key[pygame.K_x] and self.shuri_timer > 3 or key[pygame.K_DOWN] and self.shuri_timer > 3:
			self.is_attacking = True
			if self.last_dir > 0:
				self.image = self.attack_imgs[0]
			elif self.last_dir < 0:
				self.image = self.attack_imgs[1]
			self.shuri_timer = 0
			s = Shuriken(self.last_dir)
			s.rect.x = self.rect.x
			s.rect.y = self.rect.y 
			shurikens.add(s)
			scene = 1
			
		if not self.is_onground and self.last_dir > 0:
			if not self.is_attacking:
				self.image = load_image('prj.png')
		elif not self.is_onground and self.last_dir < 0:
			if not self.is_attacking:
				self.image = load_image('plj.png')
		
