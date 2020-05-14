import pygame
from pygame.locals import *
from sys import exit

#settings
pygame.init()
SCREEN_SIZE = (640, 480)
FPS = 60
TEXTCOLOR = (255, 255, 255)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("test")

#pic converting
starting = pygame.image.load( 'black.png').convert()
rescaled_starting = pygame.transform.scale(starting, SCREEN_SIZE)
background = pygame.image.load('sushiplate.jpg').convert()
mouse_cursor = pygame.image.load('fugu.png').convert_alpha()
pygame.mouse.set_visible(True)

fort = pygame.image.load('fort.png').convert_alpha()
plate = pygame.image.load('plate.png').convert_alpha()
red_center = pygame.image.load('red_center.png').convert_alpha()
red_line = pygame.image.load('red_line.png').convert_alpha()
xxx = pygame.image.load('xxx.png').convert_alpha()

#settings related to font
font = pygame.font.SysFont("arial", 18);
font_height = font.get_linesize()
event_text = []

#settings related to game
Fullscreen = False

#functions
def DisplayStr(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def init():
    global event_text

global gamestart
gamestart = True


def waitPressKey():
    global event_text
    while True:
        screen.blit(rescaled_starting, (0,0))
        DisplayStr('press to start', font, screen, SCREEN_SIZE[0] / 2 - 95, 300)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == K_RETURN:
                    init()
                    gamestart = False
                    return gamestart

#before starting game                                       
while gamestart:
    gamestart = waitPressKey()

#starting game
while True:


    #mouse setting
    x, y = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2
    screen.blit(mouse_cursor, (x, y))

    pygame.display.flip()

    
    #screen setting
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            #fullscreen (doublebuf)
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | DOUBLEBUF | FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
        screen.blit(background, (0,0))
      
        pygame.display.flip()

   
