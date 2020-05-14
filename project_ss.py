while True:
    pygame.mixer.music.play(-1)

    while True:
        ProEvent()
        AddRoles()
        RoleStatus()
        ReDraw()

        if undefended_creature >=20:
            break

        if cmWasBeat():
            break

        mainClock.tick(FPS)

    CheckWinOrLose()
    pygame.display.flip()
    waitPressKey()
    
