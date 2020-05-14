import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("test")

font = pygame.font.SysFont("arial", 18);
font_height = font.get_linesize()
event_text = []

#background_image_filename = 'sushiplate.jpg'
#mouse_image_filename = 'fugu.png'
#background = pygame.image.load(background_image_filename).convert()
#mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:

    event = pygame.event.wait()
    event_text = (str(event))
    #event_text = event_text[-SCREEN_SIZE[1]/font_height:]
    
    if event.type == QUIT:
        exit()

    screen.fill((0, 0, 0))

    y = SCREEN_SIZE[1] - font_height
    print y
    for text in revent_text[::-1]:
        if text.isalpha():
            x = random.randint(0, SCREEN_SIZE[0])
            y -= font_height
            screen.blit(font.render(text, True, (0, 255, 0), (x, y) )
    pygame.display.flip()
