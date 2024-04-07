import pygame
import random
from pygame.locals import QUIT, KEYDOWN, K_DOWN, K_UP, K_LEFT, K_RIGHT

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
tick = 90

# playground
pixel_width = 100
pixel_height = 20
startX = 590
startY = 650
score = 0
speed = 5
bat_color = (5, 255, 220)

#schläger
schlaeger_pixel = pygame.Rect(startX, startY, pixel_width, pixel_height)

# Haupt-Schleife
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        schlaeger_pixel.x -= speed
    if keys[pygame.K_RIGHT]:
        schlaeger_pixel.x += speed
    

    #Kollision mit dem Rand behandeln
    if schlaeger_pixel.left < 0:
        schlaeger_pixel.right = screen_width
    elif schlaeger_pixel.right > screen_width:
        schlaeger_pixel.left = 0

    # Bildschirm aktualisieren
    screen.fill("black")

    pygame.draw.rect(screen, bat_color, schlaeger_pixel)
    pygame.display.set_caption(f"Score: {score}")

    pygame.display.flip()

    clock.tick(tick)  # Geschwindigkeit der Schlange (je größer, desto schneller)