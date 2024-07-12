import pygame    
from constantes import *
import json
from datos import lista 

pygame.init()

#imagenes pygame
jugador_img = pygame.image.load("oi-oi-oi.png")
jugador_img_resize = pygame.transform.scale(jugador_img, (70, 70))
game_over = pygame.image.load("Game_Over_logo.png")
game_over = pygame.transform.scale(game_over, (400, 200))
heart = pygame.image.load("heart.png")
heart = pygame.transform.scale(heart, (300, 150))

#areas de los cuatro opcion
area_opcion1 = pygame.Rect(300, 100, 250, 30)
area_opcion2 = pygame.Rect(300, 140, 250, 30)
area_opcion3 = pygame.Rect(300, 180, 250, 30)
area_comenzar = pygame.Rect(200, 451, 280, 130)
area_terminar = pygame.Rect(550, 450, 280, 130)

areas_correctas_por_ronda = [
    area_opcion1,  # Ronda 1: opcion 1
    area_opcion2,  # Ronda 2: opcion 2
    area_opcion2,  # Ronda 3: opcion 2
    area_opcion2,  # Ronda 4: opcion 2
    area_opcion2,  # Ronda 5: opcion 2
    area_opcion3,  # Ronda 6: opcion 3
    area_opcion1,  # Ronda 7: opcion 1
    area_opcion1,  # Ronda 8: opcion 1
    area_opcion3,  # Ronda 9: opcion 3
    area_opcion3,  # Ronda 10: opcion 3
    area_opcion1,  # Ronda 11: opcion 1
    area_opcion3,  # Ronda 12: opcion 3
    area_opcion2,  # Ronda 13: opcion 2
    area_opcion1,  # Ronda 14: opcion 1
    area_opcion1,  # Ronda 15: opcion 1
    area_opcion2   # ronda 16: opcion 2
]

areas_incorrectas_por_ronda = [
    [area_opcion2,area_opcion3],  # Ronda 1: opcion 1
    [area_opcion1,area_opcion2],  # Ronda 2: opcion 2
    [area_opcion1,area_opcion3],  # Ronda 3: opcion 2
    [area_opcion1,area_opcion2],  # Ronda 4: opcion 2
    [area_opcion2,area_opcion3],  # Ronda 5: opcion 2
    [area_opcion1,area_opcion3],  # Ronda 6: opcion 3
    [area_opcion1,area_opcion2],  # Ronda 7: opcion 1
    [area_opcion1,area_opcion2],  # Ronda 8: opcion 1
    [area_opcion2,area_opcion3],  # Ronda 9: opcion 3
    [area_opcion1,area_opcion3],  # Ronda 10: opcion 3
    [area_opcion1,area_opcion2],  # Ronda 11: opcion 1
    [area_opcion1,area_opcion2],  # Ronda 12: opcion 3
    [area_opcion2,area_opcion3],  # Ronda 13: opcion 2
    [area_opcion1,area_opcion3],  # Ronda 14: opcion 1
    [area_opcion1,area_opcion2],  # Ronda 15: opcion 1
    [area_opcion1,area_opcion3]   # Ronda 16: opcion 2
]

def check_answer_with_areas(mouse_pos, current_question):
    # Obtener las áreas correctas e incorrectas para la ronda actual
    area_correcta = areas_correctas_por_ronda[current_question]
    areas_incorrectas = areas_incorrectas_por_ronda[current_question]

    if area_correcta.collidepoint(mouse_pos):
        return True
    for area_incorrecta in areas_incorrectas:
        if area_incorrecta.collidepoint(mouse_pos):
            return False
    return None

comenzar = pygame.Rect(200, 450, 280, 130)
terminar = pygame.Rect(550, 450, 270, 130)

def check_terminar(mouse_pos):
    if area_terminar.collidepoint(mouse_pos):
        return True

def check_comenzar(mouse_pos):
    if area_comenzar.collidepoint(mouse_pos):
        return True


screen = pygame.display.set_mode([ancho_ventana, alto_ventana])   

board = pygame.Rect(300, 3, 400, 200)
casilla1 =  pygame.Rect(300, 250, 70, 50)
casilla2 =  pygame.Rect(380, 250, 70, 50)
casilla3 =  pygame.Rect(460, 250, 70, 50)
casilla4 =  pygame.Rect(540, 250, 70, 50)
casilla5 =  pygame.Rect(620, 250, 70, 50)
avanza1 =  pygame.Rect(700, 250, 70, 50)
casilla7 =  pygame.Rect(780, 250, 70, 50)
casilla8 =  pygame.Rect(860, 250, 70, 50)
casilla9 =  pygame.Rect(860, 350, 70, 50)
casilla10 =  pygame.Rect(780, 350, 70, 50)
casilla11 =  pygame.Rect(700, 350, 70, 50)
casilla12 =  pygame.Rect(620, 350, 70, 50)
retrocede1 =  pygame.Rect(540, 350, 70, 50)
casilla14 =  pygame.Rect(460, 350, 70, 50)
casilla15 =  pygame.Rect(380, 350, 70, 50)
casilla16 =  pygame.Rect(300, 350, 70, 50)


#fuentes
font_big = pygame.font.Font(None, 40)
font_medium = pygame.font.Font(None, 28)
font_small = pygame.font.Font(None, 18)

#evento click
click = pygame.MOUSEBUTTONDOWN

#funciones de dibujo para la pantalla (estetico)

#Funcion que crea las casillas automaticamente
def crear_casillas()-> None:
    pygame.draw.rect(screen, verde_oscuro, board)
    pygame.draw.rect(screen, naranja, casilla1)
    pygame.draw.rect(screen, rojo, casilla2)
    pygame.draw.rect(screen, amarillo, casilla3)
    pygame.draw.rect(screen, verde, casilla4)
    pygame.draw.rect(screen, rosa, casilla5)
    pygame.draw.rect(screen, blanco, avanza1)       
    pygame.draw.rect(screen, aqua, casilla7)
    pygame.draw.rect(screen, azul, casilla8)
    pygame.draw.rect(screen, azul, casilla9)
    pygame.draw.rect(screen, aqua, casilla10)
    pygame.draw.rect(screen, blanco, casilla11)
    pygame.draw.rect(screen, rosa, casilla12)
    pygame.draw.rect(screen, verde, retrocede1)
    pygame.draw.rect(screen, amarillo, casilla14)
    pygame.draw.rect(screen, rojo, casilla15)
    pygame.draw.rect(screen, naranja, casilla16)
    pygame.draw.rect(screen, azul_oscuro, comenzar)
    pygame.draw.rect(screen, azul_oscuro, terminar)

#funcion que carga y dibuja las imagenes
def crear_imagenes()-> None:
    arrow = pygame.image.load("curved_arrow.png")
    resized_arrow = pygame.transform.scale(arrow, (100, 100))
    smiley_face = pygame.image.load("smiley_face.png")
    player = pygame.transform.scale(smiley_face, (70, 60))
    pre_arrow_salida = pygame.image.load("arrow_salida.png")
    arrow_salida = pygame.transform.scale(pre_arrow_salida, (90, 30))
    utn_race_load = pygame.image.load("utn_race.png")
    utn_race = pygame.transform.scale(utn_race_load, (290, 220))   

    screen.blit(resized_arrow, (910, 280))
    screen.blit(player, (200, 220))
    screen.blit(arrow_salida, (200, 285))
    screen.blit(utn_race, (1, 1))

#funcion que dibuja el texto predeterminado en la pantalla
def crear_texto()-> None:
    

    avanza1_text = font_small.render("Avanza 1", True, negro)  # True for anti-aliasing
    retrocede1_text = font_small.render("Retrocede 1", True, negro)
    volver_principio1 = font_small.render("Vuelve al", True, negro)
    volver_principio2 = font_small.render("principio", True, negro)
    comenzar_text = font_big.render("COMENZAR", True, blanco)
    terminar_text = font_big.render("TERMINAR", True, blanco)        

    screen.blit(avanza1_text, (707, 270))  
    screen.blit(retrocede1_text, (540, 370)) 
    screen.blit(comenzar_text, (250, 500))
    screen.blit(terminar_text, (610, 500))         
    screen.blit(volver_principio1, (386, 360))         
    screen.blit(volver_principio2, (389, 380))         
                   
#funcion extra para dibujar texto para utilidades
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

#Funcion principal de final del juego. Usada para pedir el Nombre del usuario luego de la partida.
def get_player_name():
    name = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # presionar la tecla ENTER -> input_active False. Se termina el bucle.
                    input_active = False
                elif event.key == pygame.K_BACKSPACE: #presionar la tecla BACKSPACE, 
                    name = name[:-1]                    #se elimina el último carácter de la variable name
                else: #presionae cualquier otra tecla -> carácter se añade al nombre. 
                    name += event.unicode   #event.unicode que contiene el carácter de la tecla presionada.

        #Creacion de la pantalla de gameover
        screen.fill(celeste)
        draw_text("Enter your name:", font_big, negro, screen, 20, 20)
        draw_text(name, font_big, negro, screen, 20, 100)
        draw_text("Ranking: ", font_big, negro, screen, 400, 50)
        ranking = cargar_datos_rank("leaderboard.json")
        ordenar_lista(ranking, "score")
        for i in range(len(ranking)):
            draw_text(f"{ranking[i]['name']}--->{ranking[i]['score']}", font_medium, negro, screen, 400, 100 + i * 40)     
        screen.blit(jugador_img, (150, 300))   
        screen.blit(game_over, (600, 50))
        screen.blit(heart, (550, 430))
        draw_text("GRACIAS POR JUGAR!", font_medium, negro, screen, 400, 500)
        
        pygame.display.flip()
    return name


#Funcion bubblesort para mayor a menor
def ordenar_lista(lista, clave):
    for i in range(len(lista) - 1):
        for j in range(0,len(lista) - i - 1):
            if lista[j][clave] < lista[j + 1][clave]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
#Funcion para guardar el score del usuario
def save_score(name, score):
    try:
        with open(leaderboard_file, 'r') as file: #Cargar el contenido del archivo en la variable 'leaderboard'
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = [] # Si el archivo no existe, inicializar 'leaderboard' como una lista vacía

    # Añadir el nuevo nombre y puntaje a la tabla de clasificación
    leaderboard.append({"name": name, "score": score})
    
    # Guardar la tabla de clasificación actualizada en el archivo
    with open(leaderboard_file, 'w') as file:
        json.dump(leaderboard, file)
#funcion para cargar
def cargar_datos_rank(path: str) -> list|None:
    datos = None # Inicializo la variable para almacenar datos
    if len(path) > 0 and type(path) == str: #La función verifica si la longitud de la cadena path es mayor que 0 y si path es una cadena str.
        try:
          with open(path, 'r', encoding="utf-8") as f:
              datos = json.load(f) # Cargar los datos del archivo en 'datos'
        except FileNotFoundError:
            datos = None  # Si el archivo no se encuentra, 'datos' permanece como None
    return datos  # Devolver los datos cargados o None si no se pudo leer el archivo

#Funciones y variables para la lista de preguntas
questions = lista
current_question = 0
options = ['a', 'b', 'c']

def check_answer(mouse_pos, correct_option, options_rects):
    for i in range(len(options_rects)):
        if options_rects[i].collidepoint(mouse_pos):  # Verifica si el mouse está dentro del rectángulo
            return i == correct_option  # Devolver True si el índice coincide con la opción correcta
    return False  # Devolver False si no hay coincidencia


def next_question(current_question, start_ticks):
    current_question += 1
    if current_question >= len(questions):
        current_question = 0
    start_ticks = pygame.time.get_ticks()
    time_left = 5
    return current_question, start_ticks, time_left

def handle_special_squares_correct(player_pos):
    if player_pos == 6:
        player_pos += 1
    elif player_pos == 13:
        player_pos -= 1
    return player_pos

def handle_special_square_reset(player_pos, score):
    if player_pos == 15:
        player_pos = 0
        score = 0
    return player_pos, score


# Función para obtener las coordenadas de la imagen
def get_image_coordinates(player_pos):
    match player_pos:
        case 0:
            return (200, 210)
        case 1:
            return (300, 200)  # Coordenadas para player_pos = 1
        case 2:
            return (380, 200)  # Coordenadas para player_pos = 2
        case 3:
            return (460, 200)  # Coordenadas para player_pos = 3
        case 4:
            return (540, 200)  # Coordenadas predeterminadas
        case 5:
            return (620, 200)  # Coordenadas predeterminadas
        case 6:
            return (700, 200)  # Coordenadas predeterminadas
        case 7:
            return (780, 200)  # Coordenadas predeterminadas
        case 8:
            return (860, 200)  # Coordenadas predeterminadas
        case 9:
            return (860, 320)  # Coordenadas predeterminadas
        case 10:
            return (780, 320)  # Coordenadas predeterminadas
        case 11:
            return (700, 320)  # Coordenadas predeterminadas
        case 12:
            return (620, 320)  # Coordenadas predeterminadas
        case 13:
            return (540, 320)  # Coordenadas predeterminadas
        case 14:
            return (460, 320)  # Coordenadas predeterminadas
        case 15:
            return (380, 320)  # Coordenadas predeterminadas
        case 16:
            return (300, 320)  # Coordenadas predeterminadas

            
        
