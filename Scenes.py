import pygame, os
from Map import *
from Player import Player
from settings import *
from Enemy import Enemy
from Effect import Smoke
from Assets import End_sign

#=================================
class Title():
	def __init__(self):
		self.next_scene = {"scene" : "scene1"}
		self.fullname = os.path.join("images", "title.png")
		self.image = pygame.image.load(self.fullname).convert()
		self.bla = pygame.event.Event(pygame.USEREVENT+1, self.next_scene)
		self.font = pygame.font.Font(None, 30)
		self.label = self.font.render("press space", 1, (0,0,0))
		
	def update(self, screen):
		screen.blit(self.image, (0,0))
		screen.blit(self.label, (300, 400))
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]:
			pygame.event.post(self.bla)
		
		


#===============================================

class Scene1():
	def __init__(self, mapname):
		self.enemy_touches = 0
		self.lives = 3
		self.player_startpos = [0,0]
		self.mapname = mapname
		self.score = 0
		self.font = pygame.font.Font(None, 30)
		self.text = self.font.render("score: " + str(self.score), 1, (255,255,255))
		self.map = map_load(self.mapname)
		self.tilemap = map_create(self.map)
		self.player = Player(self.tilemap)
		self.set_player() #set player position
		self.my_offset = [0,0]
		self.enemies = pygame.sprite.Group()
		self.enemies_load()
		self.start_scene = {"scene" : "scene0"}
		self.nextscene = {"scene" : "scene2"}
		self.bla = pygame.event.Event(pygame.USEREVENT+1, self.nextscene)
		self.end_sign = pygame.sprite.Group()
		self.end_load()
		self.life_label = self.font.render("lives: " + str(self.lives),1,(255,255,255))
		
	def end_load(self):
		for e in self.map:
			if e['code'] == "end":
				s = End_sign()
				s.rect.x = e["x"]
				s.rect.y = e["y"]
				self.end_sign.add(s)
				
	def set_score(self, s):
		self.score += s	
		
	def enemies_load(self):
		for p in self.map:
			if p['code'] == 'e':
				e = Enemy()
				e.rect.x = p['x']
				e.rect.y = p['y']
				self.enemies.add(e)
		
	def set_player(self):
		for tile in self.map:
			if tile['code'] == 'p':
				self.player.rect.x = tile['x']
				self.player.rect.y = tile["y"]
				self.player_startpos[0] = tile["x"]
				self.player_startpos[1] = tile["y"]
				
	def checkborders(self):
		if self.player.rect.x >= 320:
			self.my_offset[0] = self.player.rect.x - 320
		else:
			self.my_offset[0] = 0
		if self.player.rect.x >= 2880:
			self.my_offset[0] = 2880 - 320
		
			
		if self.player.rect.y <= 240:
			self.my_offset[1] = self.player.rect.y - 240
		else:
			self.my_offset[1] = 0
		
	def update(self, screen):
		#self.checkborders()
		self.player.update()
		
		#check collision with player and enemy
		pe = pygame.sprite.spritecollide(self.player, self.enemies, False)
		if pe:
			if self.lives > 0: #player dies
				self.lives -= 1
				self.life_label = self.font.render("lives: "+str(self.lives), 1, (255,255,255))
				self.player.rect.x = self.player_startpos[0]
				self.player.rect.y = self.player_startpos[1]
				pygame.time.delay(500)
			else:
				self.player.rect.x = self.player_startpos[0]
				self.player.rect.y = self.player_startpos[1]
				self.bla = pygame.event.Event(pygame.USEREVENT+1, self.start_scene)
				pygame.event.post(self.bla)
				
		#check collision with player and end sign
		pcol = pygame.sprite.spritecollide(self.player, self.end_sign, False)
		for c in pcol:
			pygame.time.delay(1000)
			pygame.event.post(self.bla)
		
		#check collision with shuriken and enemy
		col = pygame.sprite.groupcollide(shurikens, self.enemies, True, True)
		for c in col:
			self.set_score(50)
			self.text = self.font.render("score: " + str(self.score), 1, (255,255,255))
			s = Smoke()
			s.rect.x = c.rect.x
			s.rect.y = c.rect.y
			smokelist.add(s)
			shurikens.remove(self)
			
		#render exit scene
		for e in self.end_sign:
			screen.blit(e.image, (e.rect.x-self.my_offset[0], e.rect.y-self.my_offset[1]))
		#render player
		screen.blit(self.player.image, (self.player.rect.x - self.my_offset[0],
		 self.player.rect.y - self.my_offset[1]))
		#render smoke
		for s in smokelist:
			s.update()
			screen.blit(s.image, (s.rect.x - self.my_offset[0], s.rect.y - self.my_offset[1]))
		#render enemies
		for e in self.enemies:
			screen.blit(e.image, (e.rect.x - self.my_offset[0], e.rect.y - self.my_offset[1]))
		#render map
		for tile in self.tilemap:
			screen.blit(tile.image, (tile.rect.x - self.my_offset[0],
			 tile.rect.y - self.my_offset[1]))
		#score render
		screen.blit(self.text, (10,10))
		#render shurikens
		for s in shurikens:
			s.update()
			screen.blit(s.image, (s.rect.x - self.my_offset[0], s.rect.y - self.my_offset[1]))
		#render lives label
		screen.blit(self.life_label, (150, 10))

#------------------------------

class Scene2(Scene1):
	def __init__(self, mapname):
		super().__init__(mapname)
		self.nextscene = {"scene" : "scene3"}
		self.bla = pygame.event.Event(pygame.USEREVENT+1, self.nextscene)
		
		
	def update(self, screen):
		self.checkborders()
		super().update(screen)
		
#------------------------------------

class Scene3(Scene1):
	def __init__(self, mapname):
		super().__init__(mapname)
		
	def update(self, screen):
		self.checkborders()
		super().update(screen)
		
#-----------------------------------------
		
		
	
	



