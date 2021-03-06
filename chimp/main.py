import os, pygame, sys, time
from pygame.locals import *
import highscore
from sprites import *
from textbox import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

height = 600
width = 600

TimesHit = 0
         
def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Monkey Fever')
    pygame.mouse.set_visible(0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((88, 87, 70))
    
    added = 0 
    
    chimp = Chimp()
    fist = Fist()
    bomb = Bomb()
    game_over = Game_over()
    main_menu = MainMenu()                    
    button = StartButton()
    tbutton = TopscoreButton()
    
    menu = button, tbutton
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    render_main_menu = pygame.sprite.RenderPlain((menu))
    render_main_menu.draw(screen)
    pygame.display.flip()
    
    clock = pygame.time.Clock()
    whiff_sound = load_sound('whiff.wav')
    punch_sound = load_sound('punch.wav')
    allsprites = pygame.sprite.RenderPlain((fist, chimp, bomb)) 

    while 1:
        if not button.a:
            button.update()
            tbutton.update()
             
        if button.a:
            pygame.mouse.set_visible(0)
                 
        if main_menu.start_game:
            if pygame.font:
                b = " times punched: %d, times hit: %d" % (TimesPunched, TimesHit)
                background.fill((250, 250, 250))
                screen.blit(background, (0, 0))
                font = pygame.font.Font(None, 36)
                text = font.render(b , 1, (10, 10, 10,))
                textpos = [100, 300]
                background.blit(text, textpos)
                screen.blit(background, (0, 0))
        
        if tbutton.a:
            if not main_menu.start_game:
                highscore.print_in_browser()
                tbutton.a = 0
         
        if not main_menu.start_game:
            pygame.mouse.set_visible(1)
         
        clock.tick(60)                
         
        TimesHit = chimp.TimesHit
        TimesPunched = fist.TimesPunched     
         
        for event in pygame.event.get():    
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                if button.a == 1:
                    if button._click():
                        main_menu.start_game = 1
                    if tbutton._click():
                        a = highscore.print_all()
                        pygame.display.flip()
                if main_menu.start_game == 1:
                    if fist.punch(chimp):
                        punch_sound.play()
                        chimp.punched()
                    else:
                        whiff_sound.play()
                        
            elif event.type is MOUSEBUTTONUP:
                fist.unpunch()
                
            elif event.type == KEYDOWN and event.key == K_r:
                pygame.mouse.set_visible(0)        
                allsprites.update()
                screen.blit(background, (0, 0))
                allsprites.draw(screen)
                pygame.display.flip()        
                bomb.colliderate = 0
                fist.TimesPunched = 0
                chimp.TimesHit = 0
                added = 0 
                main_menu.start_game = 1
                
        if bomb._collider(fist):
            if main_menu.start_game:
                bomb.hit = 1
                bomb._kaboom()
                if added == 0:
                    a = ask(screen, 'Name')
                    highscore.historic(TimesHit, a)
                    added = 1
                
        if bomb.colliderate == 1:
            if main_menu:
                background.fill((0, 0, 0))
                screen.blit(background, (0, 0))
                time.sleep(1)
                pygame.display.flip()                         
                render_game_over = pygame.sprite.RenderPlain((game_over))
                render_game_over.draw(screen)
                pygame.display.flip()
                bomb.hit = 0
         
        else:                                                            
            if main_menu.start_game == 1:
                allsprites.update()
                screen.blit(background, (0, 0))
                allsprites.draw(screen)
                pygame.display.flip()       
                                
if __name__=='__main__': main()