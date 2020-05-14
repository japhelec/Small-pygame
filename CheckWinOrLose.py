def CheckWinOrLose():
    pygame.mixer.music.stop()
    gameOverSound.play()
    time.sleep(4)
    gameOverSound.stop()
    screen.blit(ending, (0,0))

    DisplayStr('Score :  %s' % (Score), font, screen, 10, 30)
    DisplayStr('press ESC to quit, press ENTER to restart', font ,screen, SCREENSIZE[0]/2 , SCREENSIZE[1]/3)

    if undefended_creature < 20:
        DisplayStr('VICTORY', font, screen, SCREENSIZE[0]/2-50, SCREENSIZE[1]/2)
        gameWinSound.play()

    else:
        DisplayStr('DEFEAT', font, screen, SCREENSIZE[0]/2-50, SCREENSIZE[1]/2)
        
