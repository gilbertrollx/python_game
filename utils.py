import pygame, os

def load_image(name):
    fullname = os.path.join('images', name)
    image = pygame.image.load(fullname).convert()
    colorkey = image.get_at((0,0))
    image.set_colorkey(colorkey)
    return image

def animate(self, imgs, speed): 
        now = pygame.time.get_ticks()
        
        if now - self.last_update > speed:
            self.last_update = now
            if self.current_frame < len(imgs):
                self.image = imgs[self.current_frame]
                self.current_frame += 1
            else:
                self.current_frame = 0

def load_sound(name):
        fullname = os.path.join('sounds', name)
        sound = pygame.mixer.Sound(fullname)
        return sound