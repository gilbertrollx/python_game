import pygame, json, os
from Enemy import Enemy
from settings import *
from utils import *

def map_load(map_name): #load json
    with open(map_name) as f:
        tile_map = json.load(f)
    return tile_map

def map_create(tilemap):#json to list of objects
    tmap = []
    for tile in tilemap:
        '''
        if tile['code'] == 'e':
            e = Enemy()
            e.rect.x = tile['x']
            e.rect.y = tile['y']
            tmap.append(e)
            enemies.add(e)
        '''
        if tile['code'] == 1:
            a = Block(load_image('block.png'))
            a.rect.x = tile['x']
            a.rect.y = tile['y']
            tmap.append(a)
        if tile['code'] == 2:
            a = Block(load_image('grass_ground.png'))
            a.rect.x = tile['x']
            a.rect.y = tile['y']
            tmap.append(a)
        if tile['code'] == 3:
            a = Block(load_image('ground.png'))
            a.rect.x = tile['x']
            a.rect.y = tile['y']
            tmap.append(a)
    return tmap


class Block(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
