#init and whatnot idk

game_over = False

#add_cars

#update_cars

#update_frog

#add_turtles

#add_logs

#update_turtles

#update_logs

#scorebox

is_collision():
    global game_over
    if pygame.sprite,spritecollideany(frog, enemy):
        game_over = True
    else:
        game_over = False

DISPLAYSURF.blit(rex.image,rex.rect)
while True:
    if game_over == True:
        frog.kill()
        cars.kill()
        turtle.kill()
        log.kill()
    if event.type==KEYDOWN:
        if event.key==K_UP:
            x.up(150)
        if event.key==K_DOWN:
            x.down(150)
        if event.key==K_LEFT:
            x.left(150)
        if event.key==K_RIGHT:
            x.right(150)
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

    #blah blah blah etc
