import pygame
from datos import lista
from constantes import *
from rect import *


pygame.init() #Se inicializa pygame


screen = pygame.display.set_mode([ancho_ventana, alto_ventana]) #Se crea una ventana
pygame.display.set_caption("Test") #Titulo de la ventana
icono = pygame.image.load("Trollface.jpg")
pygame.display.set_icon(icono)

player_pos = 0
score = 0
time_left = 5
leaderboard_file = 'leaderboard.json'
total_positions = 17
seconds = 5
remaining_game_time = 5


start_ticks = pygame.time.get_ticks()
game_starts_ticks = pygame.time.get_ticks()
total_game_time = 10 #2 min
jugador_img = pygame.image.load("oi-oi-oi.png")
jugador_img = pygame.transform.scale(jugador_img, (100, 100))
jugador_rect = jugador_img.get_rect()
jugador_rect.topleft = (200, 200)


pygame.display.flip()# Muestra los cambios en la pantalla



pause = True

while running: # Se verifica si el usuario cerro la ventana
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == click:
            x = event.pos[0]
            y = event.pos[1]
            x_aux = x
            y_aux = y
            print(f"\nx:{x_aux} y:{y_aux}")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            anashi = check_comenzar(mouse_pos)
            if anashi == True:
                
                if pause == True:
                    start_ticks = pygame.time.get_ticks()
                    game_starts_ticks = pygame.time.get_ticks()
                pause = False
            if  pause == False:  
                question_data = questions[current_question]
                
                result = check_answer_with_areas(mouse_pos, current_question)
                
                if result == True:
                    player_pos += 2
                    score += 10
                    player_pos = handle_special_squares_correct(player_pos)
                    current_question, start_ticks, time_left = next_question(current_question, start_ticks)
                    print("click correcto")
                elif result == False:
                    player_pos -= 1
                    current_question, start_ticks, time_left = next_question(current_question, start_ticks)
                    print("Click incorrecto")
                    if player_pos < 0:
                        player_pos = 0 
                          # Asegurarse de que la posición del jugador no sea negativa
                elif result == None:
                    print("click fuera")
                    
                
                if player_pos >= total_positions:  # Condición de finalización del juego
                    running = False
                    player_name = get_player_name()
                    save_score(player_name, score)
                    break
                
                terminar = check_terminar(mouse_pos)
                
                if terminar == True:
                    running = False
                    player_name = get_player_name()
                    save_score(player_name, score)
                    break

            

        
    
    
    if pause == False:    
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds > time_left:
            current_question, start_ticks, time_left = next_question(current_question, start_ticks)

        total_elapsed_seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        remaining_game_time = total_game_time - total_elapsed_seconds

        # Verificar si el tiempo total ha expirado
        if remaining_game_time <= 0:
            running = False
            player_name = get_player_name()
            save_score(player_name, score)
            break
    
        player_pos, score = handle_special_square_reset(player_pos, score)
    
    screen.fill(celeste)
        
    crear_casillas()
    crear_imagenes()
    crear_texto()
    pygame.draw.rect(screen, (0,0,255), area_opcion1)
    pygame.draw.rect(screen, (0,255,255), area_opcion2)
    pygame.draw.rect(screen, (255,0,255), area_opcion3)
    
    image_coords = get_image_coordinates(player_pos)

    # Dibujar la imagen en la nueva posición
    if image_coords != None:
        screen.blit(jugador_img_resize, image_coords)


    question_data = questions[current_question]
    draw_text(question_data["pregunta"], font_medium, negro, screen, 300, 50)
    for i in range(3):
        draw_text(f"{options[i]}. {question_data[options[i]]}", font_medium, negro, screen, 300, 100 + i * 40)
    draw_text(f"Tiempo: {int(time_left - seconds)}", font_big, negro, screen, 800, 20)
    draw_text(f"Reloj: {int(remaining_game_time )}", font_big, negro, screen, 100, 300)
    draw_text(f"Puntaje: {score}", font_big, negro, screen, 800, 60)
    draw_text(f"Posición: {player_pos}", font_big, negro, screen, 600, 140)
    
    
    pygame.display.flip()
    
pygame.quit() # Fin