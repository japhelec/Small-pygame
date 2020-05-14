import pygame
import time
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
import math
pygame.init()
#setting========================================
SCREEN_SIZE = (640, 480)
FPS = 60
TEXTCOLOR = (255, 255, 255)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("test")
#picconverting===================================
starting = pygame.image.load( 'black.png').convert()
rescaled_starting = pygame.transform.scale(starting, SCREEN_SIZE)
background = pygame.image.load('sushiplate.jpg').convert()
mouse_cursor = pygame.image.load('fugu.png').convert_alpha()
pygame.mouse.set_visible(True)

fort = pygame.image.load('fort.png').convert_alpha()
plate = pygame.image.load('plate.png').convert_alpha()
gun = pygame.image.load('06.png').convert_alpha()
player = pygame.image.load('02.png').convert_alpha()
ball = pygame.image.load('05.png').convert_alpha()
cm = pygame.image.load('08.png').convert_alpha()
yota = pygame.image.load('10.png').convert_alpha()
ta = pygame.image.load('09.png').convert_alpha()
xxx = pygame.image.load('xxx.png').convert_alpha()

youwin = pygame.image.load('youwin.jpg').convert_alpha()
gameover = pygame.image.load('gameover.jpg').convert_alpha()
#initial>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
        DisplayStr('press ENTER to start', font, screen, SCREEN_SIZE[0] / 2 - 95, 300)
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
                    
def CheckWinOrLose():
#    pygame.mixer.music.stop()
#    gameOverSound.play()
#    time.sleep(4)
#    gameOverSound.stop()
    screen.blit(starting, (0,0))

    DisplayStr('Score :  %s' % (Score), font, screen, 10, 30)
    DisplayStr('press ESC to quit, press ENTER to restart', font ,screen, SCREEN_SIZE[0]/2 , SCREEN_SIZE[1]/3)

    if undefended_creature < 20:
        DisplayStr('VICTORY', font, screen, SCREEN_SIZE[0]/2-50, SCREEN_SIZE[1]/2)
        screen.blit(youwin, (0,0))
#        gameWinSound.play()

    else:
        DisplayStr('DEFEAT', font, screen, SCREEN_SIZE[0]/2-50, SCREEN_SIZE[1]/2)
        screen.blit(gameover, (0,0))

    pygame.display.flip()

global judge
judge = True

def game_cursor():
    while True:
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
                    return judge

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#definition================for (ball,cm,ta,yota)=====================================================================================================
#player
undefended_creature = 0
Score = 0

#cannon&fort
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
playerpos=[100,100]
acc=[0,0]
arrows=[]
player = pygame.image.load("02.png")
#castle = pygame.image.load("01.png")
#grass = pygame.image.load("03.png")
plate = pygame.image.load("04.png")
#arrow = pygame.image.load("05.png")
gun = pygame.image.load("06.png")
fort = pygame.image.load("07.png")

#ball
sprite_image_filename_ball = '05.png'
screen = pygame.display.set_mode((640,480))
#background = screen
clock = pygame.time.Clock()
sprite_image_filename_ball = pygame.image.load(sprite_image_filename_ball).convert_alpha()
position_ball = Vector2(150,150)
position_ball_set = []
position_ball_set.append(position_ball)
position_ball_set_1=[]
position_ball_set_1.append(position_ball)
speed_ball_x = [1.5]
speed_ball_y = [-0.4]
speed = 3.0
timer_ball = 0
time_set_ball = [0]

#cm
sprite_image_filename_cm = '08.png'
screen = pygame.display.set_mode((640,480))
background = screen
clock = pygame.time.Clock()
sprite_image_filename_cm = pygame.image.load(sprite_image_filename_cm).convert_alpha()
position_cm = Vector2(640,100)
position_cm_set = []
position_cm_set.append(position_cm)
position_cm_set_1=[]
position_cm_set_1.append(position_cm)
speed_cm_x = 0.4
speed_cm_y =-0.4
time_set_cm = [0]
timer_cm = 0
health_cm = 10
#ta
sprite_image_filename_ta = '09.png'
screen = pygame.display.set_mode((640,480))
#background = screen
clock = pygame.time.Clock()
sprite_image_filename_ta  = pygame.image.load(sprite_image_filename_ta ).convert_alpha()
position_ta = Vector2(620.0,390.0)
position_ta_set = []
position_ta_set.append(position_ta)
position_ta_set_1=[]
position_ta_set_1.append(position_ta)
speed_ta_x = 0.4
speed_ta_y =-0.4
timer = 0
time_set_ta = [0]
#yota
sprite_image_filename_yota = '10.png'
screen = pygame.display.set_mode((640,480))
#background = screen
clock = pygame.time.Clock()
sprite_image_filename_yota  = pygame.image.load(sprite_image_filename_yota).convert_alpha()
position_yota = Vector2(620.0,460.0)
position_yota_set = []
position_yota_set.append(position_yota)
position_yota_set_1=[]
position_yota_set_1.append(position_yota)
speed_yota_x = 0.4
speed_yota_y =-0.4
gravitation = []
gravitation.append(1.5)
timer_yota = 0
time_set_yota = [0]


#before starting game                                       
while gamestart:
    gamestart = waitPressKey()
#game work=======================================================================================================================================

while 1:
#    judge = game_cursor()
    while True:
        for event in pygame.event.get():
           if event.type == QUIT:
               exit()
        screen.fill(0)
#cannon
        screen.blit(player, (100,100))
        position=pygame.mouse.get_pos()
        angle = math.atan2(position[1]-(playerpos[1]),position[0]-(playerpos[0]))
        playerrot = pygame.transform.rotate(player, 360-angle*57.29)
        playerpos1 = (playerpos[1]-playerrot.get_rect().width/2+58, playerpos[1]-playerrot.get_rect().height/2+58)
        screen.blit(playerrot, playerpos1)
        screen.blit(plate,(45,45))
        screen.blit(gun,(150,150))
        screen.blit(fort,(10,400))
#ball
        time_passed = clock.tick()
        time_number_ball = len(time_set_ball)
        k=0
        while k < time_number_ball:
            time_set_ball[k] += time_passed
            k += 1
        timer_ball += time_passed
        if timer_ball > 1500 :
            timer_ball = 0
            time_set_ball.append(0)
            position_ball_set.append((150,150))
            position = pygame.mouse.get_pos()
            angle = math.atan2(position[1]-100,position[0]-100)
            speed_coordinate_x = speed*math.cos(angle)
            speed_coordinate_y = speed*math.sin(angle)
            speed_ball_x.append(speed_coordinate_x)
            speed_ball_y.append(speed_coordinate_y)
        i=0
        position_number_ball = len(position_ball_set)
        while i < position_number_ball :
            position_ball_set[i] += Vector2(speed_ball_x[i]*time_set_ball[i]/1000.0, speed_ball_y[i]*time_set_ball[i]/1000.0+0.5*2.0*time_set_ball[i]/1000.0*time_set_ball[i]/1000.0)
            screen.blit(sprite_image_filename_ball,position_ball_set[i])
            i+=1
        if  len(position_ball_set) > 0:
            determinant_ball_x = position_ball_set[0][0]
            determinant_ball_y = position_ball_set[0][1]
            if determinant_ball_x > 640 or determinant_ball_y  > 480:
                del position_ball_set[0]
                del time_set_ball[0]
                del speed_ball_x[0]
                del speed_ball_y[0]
#cm
        timer_cm += time_passed
        if undefended_creature >= 10:
            if len(position_cm_set) >0:
                time_set_cm[0] += time_passed
                position_cm_set[0] = position_cm_set_1[0]+((-1)*3.5*time_set_cm[0]*20/1000.0,25*math.cos(4.0*time_set_cm[0]/1000.0))
                screen.blit(sprite_image_filename_cm,(position_cm_set[0][0],position_cm_set[0][1]))
#                determinant_ta = position_ta_set[0][0]
                determinant_cm = position_cm_set[0][0]
                if determinant_cm < 10:
                    del position_cm_set[0]
                    del time_set_cm[0]
                    undefended_creature += 10
            
#ta

        time_number_ta = len(time_set_ta)
        k=0
        while k < time_number_ta:
            time_set_ta[k] += time_passed
        
            k += 1
        timer += time_passed  
        if timer > 10000:
            timer = 0
            time_set_ta.append(0)
            position_ta_set.append((620.0,390.0))
            position_ta_set_1.append((620.0,390.0))
        i=0
        position_number_ta = len(position_ta_set)
        while i < position_number_ta :
            position_ta_set[i] = Vector2(620.0,390.0)+Vector2((-1)*2.8*time_set_ta[i]*30.0/1000.0,70.0*math.cos(4.0*time_set_ta[i]/1000.0)*math.cos(4.0*time_set_ta[i]/1000.0))
            screen.blit(sprite_image_filename_ta,(position_ta_set[i][0],position_ta_set[i][1]))
            i+=1
        if len(position_ta_set)>0:
            determinant_ta = position_ta_set[0][0]
            if determinant_ta < 10:
                del position_ta_set[0]
                del time_set_ta[0]
                undefended_creature += 1
#yota
        if timer_cm>10000: 
            time_number_yota = len(time_set_yota)
            k=0
            while k < time_number_yota:
                time_set_yota[k] += time_passed
                k += 1
            timer_yota += time_passed   
            if timer_yota > 10000:
                timer_yota = 0
                time_set_yota.append(0)
                position_yota_set.append((620.0,300.0))
                position_yota_set_1.append((620.0,300.0))
            i=0
            position_number_yota = len(position_yota_set)
            while i < position_number_yota :
                position_yota_set[i] = Vector2(620.0,300.0)+Vector2((-1)*time_set_yota[i]/1000.0*90,0)
                screen.blit(sprite_image_filename_yota,(position_yota_set[i][0],position_yota_set[i][1]))
                i+=1
            if len(position_yota_set)>0:
                determinant_yota = position_yota_set[0][0]
                if determinant_yota < 10:
                    del position_yota_set[0]
                    del time_set_yota[0]
                    undefended_creature += 2
#determinant:
        m = 0
        n = len(position_ball_set)
        while m < n:
            x = 0
            y = len(position_ta_set)
            while x < y:
                if len(position_ta_set)>0:
                    ball_ta = position_ball_set[m] - position_ta_set[x]
                    magnitude_ball_ta = ball_ta.get_magnitude()
                    if magnitude_ball_ta < 30:
                        del position_ta_set[x]
                        del time_set_ta[x]
                        del position_ball_set[m]
                        del time_set_ball[m]
                        del speed_ball_x[m]
                        del speed_ball_y[m]
                        Score += 1
                x += 1
            m += 1
        m=0
        n=len(position_ball_set)
        while m < n:
            a = 0
            b = len(position_yota_set)
            while a < b:
                if len(position_yota_set)>0:
                    ball_yota = position_ball_set[m] - position_yota_set[a]
                    magnitude_ball_yota = ball_yota.get_magnitude()
                    if magnitude_ball_yota < 30:
                        del position_yota_set[a]
                        del time_set_yota[a]
                        del position_ball_set[m]
                        del time_set_ball[m]
                        del speed_ball_x[m]
                        del speed_ball_y[m]
                        Score += 2
                a += 1
            m += 1
        m = 0
        n = len(position_ball_set)
        if undefended_creature >= 10:
            while m < n:
                if len(position_cm_set)>0:
                    ball_cm = position_ball_set[m] - position_cm_set[0]
                    magnitude_ball_cm = ball_cm.get_magnitude()
                    if magnitude_ball_cm < 30:
                        health_cm -= 1
                        if health_cm == 0:
                            del position_cm_set[0]
                            del time_set_cm[0]
                            del position_ball_set[m]
                            del time_set_ball[m]
                            del speed_ball_x[m]
                            del speed_ball_y[m]
                            Score += 10
                m += 1
        DisplayStr('Health:%s'%(20-int(undefended_creature)),font,screen,10,20)
        DisplayStr('Score:%s'%(Score),font,screen,10,50)
#whether the game is over:
        if undefended_creature >= 20:
            break
        if len(position_cm_set) == 0:
            break
    

    
        pygame.display.flip() 


#check win or lose:

    CheckWinOrLose()
    pygame.display.flip()
#    time.sleep(10)

    

