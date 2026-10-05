import pygame
#from screeninfo import get_monitors

pygame.init()

gravity = 0.5
velocity_y = 0
speed = 2
screen_width = 1200
screen_height = 600
sqr = 50
screen1 = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("grunig")
screen2 = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
player = pygame.Rect((sqr, sqr, sqr, sqr))
center = screen_height/2 , screen_width/2
cursor_pos = 0, 0
fullscreen = True
run = True
player_y = float(player.y)
menu_change = 1
switch = 0
currentscreen = screen1
pygame.mouse.set_visible(True)



while run:
    
    pygame.draw.rect(currentscreen, ((225, 225, 225)), player)
    player_pos = player.x, player.y
    key = pygame.key.get_pressed()

    cursor_pos = pygame.mouse.get_pos()

    player.x, player.y = cursor_pos
    player.x, player.y = player.x - sqr/2, player.y - sqr/2



    if key[pygame.K_m] == True:

        if menu_change:
            screen2.fill((255, 0, 0))
            pygame.draw.rect(screen2, ((225, 225, 225)), player)
            currentscreen = screen2
            menu_change = 0
        else:
            screen1.fill((0, 0, 255,))
            pygame.draw.rect(screen1, ((225, 225, 225)), player)
            currentscreen = screen1
            menu_change = 1

    pygame.display.update()


    if key[pygame.K_ESCAPE] == True or key[pygame.K_q] == True:
        run = False 
       
    if key[pygame.K_F11] == True:
        if fullscreen:
            currentscreen = pygame.display.set_mode((screen_width, screen_height))
            fullscreen = False
            pygame.time.delay(200)

        else:
            currentscreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            fullscreen = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()





"""
    if key[pygame.K_w] == True or key[pygame.K_UP] == True:
        if player.top > 0:
            player.move_ip(0, -speed)

    if key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
        if player.bottom < screen_height:
            player.move_ip(0, speed)
 
    if key[pygame.K_a] == True or key[pygame.K_LEFT] == True:
        if player.left > 0:
            player.move_ip(-speed, 0)

    if key[pygame.K_d] == True or key[pygame.K_RIGHT] == True:
        if player.right < screen_width:
            player.move_ip(speed, 0)

    if key[pygame.K_ESCAPE] == True or key[pygame.K_q] == True:
        run = False  
    
    if key[pygame.K_0] == True:
        player.y, player.x = center

    if key[pygame.K_f] == True:
       if fullscreen:
           screen = pygame.display.set_mode((screen_width, screen_height))
           fullscreen = False
           pygame.time.delay(200)

       else:
           screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
           fullscreen = True
""" 