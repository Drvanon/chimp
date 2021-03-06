'''
Created on Jan 13, 2012

@author: drvanon
'''
import pygame, os
from pygame.locals import *

TimesPunched = 0
height = 600
width = 600

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image: ", fullname
        raise SystemExit, message
    image = image.convert()
    
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
    
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()        
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message 
    return sound


class Fist(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('fist.png', -1)
        self.punching = 0
        self.TimesPunched = 0
        
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5, 10)
            
    def punch(self, target):
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5, -5)
            self.TimesPunched = self.TimesPunched + 1
            return hitbox.colliderect(target.rect)
            return TimesPunched
            
    def unpunch(self):
        self.punching = 0
                                      
class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bomb.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 400, 300
        self.move = [4, 5]
        self.hit = 0
        self.colliderate = 0
           
    def _collider(self, target):        
        hitbox = self.rect.inflate(-5, -5)
        return hitbox.colliderect(target.rect)
        
        
    def update(self):
        if self.hit:
            self._kaboom()
        else:
            self._move()
            
    def _move(self):
        newpos = self.rect.move((self.move[0], self.move[1]))
        if self.rect.left < self.area.left or \
           self.rect.right > self.area.right:
            self.move[0] = -self.move[0]
            newpos = self.rect.move((self.move))            
        self.rect = newpos
        if self.rect.top < 0 or self.rect.bottom > height:
            self.move[1] = -self.move[1]
            
    def _kaboom(self):                                  
        self.colliderate = 1                                        
        pygame.mouse.set_visible(1) 
                       
class Chimp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('chimp.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9
        self.dizzy = 0
        self.TimesHit = 0
        
    def update(self):
        if self.dizzy:
            self._spin()
        else:
            self._walk()
            
    def _walk(self):
        newpos = self.rect.move((self.move, 0))
        if self.rect.left < self.area.left or \
           self.rect.right > self.area.right:
            self.move = -self.move
            newpos = self.rect.move((self.move, 0))
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos
        
    def _spin(self):
        center = self.rect.center
        self.dizzy = self.dizzy + 12
        if self.dizzy >= 360:
            self.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)
        
    def punched(self):
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image
            self.TimesHit = self.TimesHit + 1
               

class Game_over(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('game_over.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 0, 0

class MainMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.start_game = 0
        
    def _ButtonClicked(self):
        self.start_game = 1
        
class TopscoreButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('tbutton.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 160, 80
        self.a = 0
    
    def update(self):
        self._click()
        
    def _click(self):
        hitbox = self.rect.inflate(-5, -5)
        pos = pygame.mouse.get_pos()
        if hitbox.collidepoint(pos):
            self.a = 1
            return True         

class StartButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('button.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 160, 0
        self.a = 0
    
    def update(self):
        self._click()
        
    def _click(self):
        hitbox = self.rect.inflate(-5, -5)
        pos = pygame.mouse.get_pos()
        if hitbox.collidepoint(pos):
            self.a = 1    
            return True  
