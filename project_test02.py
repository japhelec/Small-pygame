import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'

pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
pygame.display.set_caption("test")
background = pygame.image.load(background_image_filename).convert()

Fullscreen = False

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type ==VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
            pygame.display.set_caption("Window resized to " + str(event.size))

        screen_width, screen_height = SCREEN_SIZE

        for y in range(0, screen_height, background.get_height()):
            for x in range(0, screen_width, background.get_width()):
                screen.blit(background, (x, y))
                
        #if event.type == KEYDOWN:
          #  if event.key == K_f:
            #    Fullscreen = not Fullscreen
            #    if Fullscreen:
             #       screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
             #   else:
             #       screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

        #screen.blit(background, (0,0))
        pygame.display.update()
