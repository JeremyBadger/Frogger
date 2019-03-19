#init and whatnot idk

#define everything whoever wants to do that

#add_cars

#update_cars

#update_frog

#add_turtles

#add_logs

#update_turtles

#update_logs

#scorebox

#is_collision


while True:
    if event.type==KEYDOWN:
        if event.key==K_UP:
            x.up(150)
            DISPLAYSURF.blit(rex.image,rex.rect)
        if event.key==K_DOWN:
            x.down(150)
            DISPLAYSURF.blit(rex.image,rex.rect)
        if event.key==K_LEFT:
            x.left(150)
            DISPLAYSURF.blit(rex.image,rex.rect)
        if event.key==K_RIGHT:
            x.right(150)
            DISPLAYSURF.blit(rex.image,rex.rect)
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

    #blah blah blah etc
