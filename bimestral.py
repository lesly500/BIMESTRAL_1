import pygame
from random import randint

pygame.init()

ANCHURA_VENTANA = 600
ALTURA_VENTANA = 600

COLOR_FONDO = (255, 255, 250)
PANTALLA = pygame.display.set_mode((ALTURA_VENTANA, ANCHURA_VENTANA))

# Bucle de control del juego
PARAR_JUEGO = False

# Variables del cohete
XX_COHETE = 210
YY_COHETE = 300
ALTURA_COHETE = 32
ANCHURA_COHETE = 32
MOVIMIENTO_XX_COHETE = 0

# Variables de los planetas
XX_PLANETA = randint(30, 130)
YY_PLANETA = 20
ALTURA_PLANETA = 32
ANCHURA_PLANETA = 32
XX_ENTRE_PLANETAS = 350
YY_ENTRE_PLANETA = 125
VELOCIDAD_PLANETAS = 2

# Puntos y texto
PUNTOS = 0
FUENTE = pygame.font.Font(None, 24)
MARCADOR = FUENTE.render("0 puntos", 1, (255, 0, 0))

# Imágenes
IMG_COHETE = pygame.image.load("img/COHETE.png")
IMG_PLANETA_IZQUIERDO = pygame.image.load("img/PLANETA.png")
IMG_PLANETA_DERECHO = pygame.image.load("img/PLANETA.png")

pygame.display.set_caption("PRIMER JUEGO")

while not PARAR_JUEGO:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PARAR_JUEGO = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                PARAR_JUEGO = True
            elif event.key == pygame.K_RIGHT:
                MOVIMIENTO_XX_COHETE = 4
            elif event.key == pygame.K_LEFT:
                MOVIMIENTO_XX_COHETE = -4
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                MOVIMIENTO_XX_COHETE = 0

    # Actualización de la posición del cohete con límites
    XX_COHETE = max(0, min(XX_COHETE + MOVIMIENTO_XX_COHETE, ANCHURA_VENTANA - ANCHURA_COHETE))

    # Dibujar fondo y objetos
    PANTALLA.fill(COLOR_FONDO)
    PANTALLA.blit(IMG_PLANETA_IZQUIERDO, (XX_PLANETA, YY_PLANETA))
    PANTALLA.blit(IMG_PLANETA_DERECHO, (XX_PLANETA + XX_ENTRE_PLANETAS, YY_PLANETA + YY_ENTRE_PLANETA))

    # Movimiento de los planetas
    YY_PLANETA += VELOCIDAD_PLANETAS
    if YY_PLANETA > ANCHURA_VENTANA:
        XX_PLANETA = randint(55, 150)
        YY_PLANETA = 25
        PUNTOS += 1
        MARCADOR = FUENTE.render(f"{PUNTOS} puntos", 1, (255, 0, 0))

   
    if XX_PLANETA + ALTURA_PLANETA > XX_COHETE and YY_PLANETA + ANCHURA_PLANETA > YY_COHETE:
        if YY_PLANETA + ANCHURA_PLANETA < YY_COHETE + ANCHURA_COHETE:
            PARAR_JUEGO = True


    if XX_PLANETA + XX_ENTRE_PLANETAS < XX_COHETE + ALTURA_COHETE and YY_PLANETA + YY_ENTRE_PLANETA + ANCHURA_PLANETA > YY_COHETE:
        if XX_PLANETA + XX_ENTRE_PLANETAS + ANCHURA_PLANETA > XX_COHETE:
            PARAR_JUEGO = True


    PANTALLA.blit(MARCADOR, (20, 580))
    PANTALLA.blit(IMG_COHETE, (XX_COHETE, YY_COHETE))
    pygame.display.update()