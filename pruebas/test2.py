import pygame

pygame.init()
ancho_ventana = 800 #constante
alto_ventana = 600 #constante

screen = pygame.display.set_mode((ancho_ventana, alto_ventana))

player = pygame.Rect((300, 250, 50, 50))
player2 = pygame.Rect((500, 250, 50, 50))
pygame.display.set_caption("TEST")
running = True


while running:

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 170, 0) , player)
    pygame.draw.rect(screen, (0, 0, 255) , player2)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    # elif key[pygame.K_a] == True and key[pygame.K_s] == True:
    #     player.move_ip(-1, 1)     No funciona

    if key[pygame.K_LEFT] == True:
        player2.move_ip(-1, 0)
    if key[pygame.K_RIGHT] == True:
        player2.move_ip(1, 0)
    if key[pygame.K_UP] == True:
        player2.move_ip(0, -1)
    if key[pygame.K_DOWN] == True:
        player2.move_ip(0, 1)
    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False



    
    pygame.display.flip()

pygame.quit()
