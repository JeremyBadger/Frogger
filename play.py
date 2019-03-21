#init and whatnot idk

#define everything whoever wants to do that
game_over = False

#add_cars

#update_cars

#update_frog

#add_turtles

#add_logs

#update_turtles

#update_logs

#scorebox

def is_collision():
    global game_over
    #if pygame.sprite.spritecollideany(frog, enemy):
        #game_over == True
        #display_message("Game over")


def win():
    global game_over
    #if frog.x => 0 and frog.x <= 24:
        #game_over == True
        #display_message("Win")

while True:
    if game_over == False:
        #draw frog
        #add_cars
        #update_cars
        #update_frog
        #add_turtles
        #update_turtles
        #add_logs
        #update_logs
        #scorebox
        is_collision()
        win()
    elif game_over == True:
        #frog.kill()
        #car.kill()
        #log.kill()
        #turtle.kill()
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
