# 1 - Import library
import pygame, time
from pygame.locals import *
import math 
import time
from gameobjects.vector2 import Vector2
pygame.init()
# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
playerpos=[100,100]
acc=[0,0]
arrows=[]
clock = pygame.time.Clock()
time = []
# 3 - Load images
player = pygame.image.load("02.png")
castle = pygame.image.load("01.png")
grass = pygame.image.load("03.png")
plate = pygame.image.load("04.png")
arrow = pygame.image.load("05.png")
gun = pygame.image.load("06.png")
fort = pygame.image.load("07.png")
#time_passed_all = 1
#clock = pygame.time.Clock()
#time_set = [0]
sprite_image_filename = '05.png'
#screen = pygame.display.set_mode((640,480))
#background = screen
clock = pygame.time.Clock()
sprite_image_filename = pygame.image.load(sprite_image_filename).convert_alpha()

position_boss = Vector2(100,100)
position_boss_set = []
position_boss_set.append(position_boss)
speed_boss_x = [1.5]
speed_boss_y = [-0.4]
speed = 1.55

time_set = [0]


# 4 - keep looping through
while 1:
#	time_passed = clock.tick()
#	time_passed_all += time_passed
 
   # 5 - clear the screen before drawing it again
	screen.fill(0)
    # 6 - draw the screen elements
#	screen.blit(castle, (100,150))
	screen.blit(player, (100,100))
	position=pygame.mouse.get_pos()
	angle = math.atan2(position[1]-(playerpos[1]),position[0]-(playerpos[0]))
	playerrot = pygame.transform.rotate(player, 360-angle*57.29)
	playerpos1 = (playerpos[1]-playerrot.get_rect().width/2+58, playerpos[1]-playerrot.get_rect().height/2+58)
	screen.blit(playerrot, playerpos1)
	screen.blit(plate,(45,45))
	screen.blit(gun,(150,150))
	screen.blit(fort,(10,400))
	# 6.2 - Draw arrows
#	for bullet in arrows:
#	        index=0
#	        velx=math.cos(bullet[0])*15
#	        vely=math.sin(bullet[0])*20
#	        bullet[1]+= velx
#	        bullet[2]+= vely
#	        if bullet[1]>640 or bullet[2]>480:
#           		 arrows.pop(index)
#	       	index+=1
#	number = len(arrows)
#	i=0
#	while i < number:
		
#	        for projectile in arrows:
#		        arrow1 = pygame.transform.rotate(arrow, angle)
#		        screen.blit(arrow1, (projectile[1], projectile[2]))
#	for projectile in arrows:
#		        projectile[1] = projectile[1]+velx*t
#		        projectile[2] = projectile[2]+vely*t+0.5*3*t*t
#		screen.blit(arrow1, (projectile[1], projectile[2]))
#	print (time_passed_all)
    # 7 - update the screen
	pygame.display.flip()
    # 8 - loop through the events
	for event in pygame.event.get():
        # check if the event is the X button 
		if event.type==pygame.QUIT:
            # if it is quit the game
#			pygame.quit() 
			exit(0)
#		if event.type==pygame.MOUSEBUTTONDOWN:
#                        acc[1]+=1
#                        arrows.append([angle,150,150])
	screen.fill(0)
	time_passed = clock.tick()
	time_number = len(time_set)

	k=0
	while k < time_number:
		time_set[k] += time_passed
		k += 1
	if time_set[0] > 500 :
		position_boss_set.append(position_boss)
		time_set[0] = 0
		time_set.append(0)
		position_boss_set.append((150.0,150.0))
		position = pygame.mouse.get_pos()
		angle = math.atan2(position[1]-100.0,position[0]-100.0)
		coordinate_x = speed*math.cos(angle)
		coordinate_y = speed*math.sin(angle)
		speed_boss_x.append(coordinate_x)
		speed_boss_y.append(coordinate_y)
	i=0
	time_number = len(time_set)
	while i < time_number-1 :
		position_boss_set[i] += Vector2(speed_boss_x[i]*(2)*time_set[i+1]/1000.0, speed_boss_y[i]*(2.3)*time_set[i+1]/1000.0+0.5*3.0*time_set[i+1]/1000.0*time_set[i+1]/1000.0)
		screen.blit(sprite_image_filename,position_boss_set[i])

		i+=1

	i=0
	j=len(position_boss_set)
	aux = []
	while i < j:
		vector1 =  position_boss_set[i] - Vector2(640.0,400.0)
		magnitude = vector1.get_magnitude()
		if magnitude < 10:
			aux.append(i)
		i+=1
	aux.reverse()
	for k in aux:
		position_boss_set.pop(k)
	pygame.display.update()
