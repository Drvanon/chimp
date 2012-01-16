import pygame
from pygame.locals import *

def get_key():
    event = pygame.event.poll()
    if event.type == KEYDOWN:
        return event.type
    else:
        pass
    
def display_box(screen, message):
    fontobject = pygame.font.Font(None,18)
    pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
    pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.flip()
    
def ask(screen, question):
    pygame.font.init()
    current_string = []
    string = []
    display_box(screen, question + ": " + string.join(current_string))
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
            b = ''
            for letters in string:
                b = b + letters 
            display_box(screen, question + ": " + b.join(current_string,""))
            return string.join(current_string, "")