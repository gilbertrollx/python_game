import pygame, Scenes, copy
from settings import *

pygame.mixer.init(11025,-16,2,512)
pygame.init()
screen = pygame.display.set_mode((640,480))
#screen = pygame.display.set_mode((640,480), pygame.FULLSCREEN)
clock = pygame.time.Clock()
run = True

scene0 = Scenes.Title()
scene1 = Scenes.Scene1("playtest.json")
scene2 = Scenes.Scene2("map001.json")
scene3 = Scenes.Scene3("mapok.json")
scenes = { "scene0" : scene0, "scene1" : scene1, "scene2" : scene2, "scene3" : scene3 }

scene = scenes["scene0"]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.USEREVENT+1:
            scene = copy.copy(scenes[event.__dict__["scene"]])
            
    screen.fill((10,100,200))
    scene.update(screen)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
