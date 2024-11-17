import time

import pygame

from settings import set_screen, SW, SH, FPS
from particles import create_particles, generate_particles

pygame.init()
clock = pygame.time.Clock()
screen, size, screen_rect = set_screen((SW, SH), 'Fireplace')

last_time = time.time()

running = True

particles = pygame.sprite.Group()

while running:

    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    screen.fill(pygame.Color('black'))

    # create_particles((SW // 2, SH // 2),
    #                  generate_particles('particle'),
    #                  1, 120,
    #                  particles)

    # particles.update(screen_rect, dt)

    screen.fill(pygame.Color('black'))
    # pygame.display.set_caption(str(clock.get_fps()))

    # particles.draw(screen)

    pygame.display.update()
    clock.tick(FPS)



pygame.quit()
