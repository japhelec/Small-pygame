def Redraw():
    screen.blit(background, (0, 0))

    screen.blit(item_image, itemRect)

    for z in creature_list:
        screen.blit(z['surface'], z['rect'])

    for o in obj_list:
        screen.blit(o['surface'], o['rect'])

    DisPlayStr('Health :  %s' % (20 - int(undefended_creature)), font, screen, 10, 20)
    DisPlayStr('Score :  %s' % (Score), font, screen, 10, 50)

    pygame.display.flip()
