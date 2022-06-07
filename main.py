import pygame
from typing import Final
import numpy as np
from classes.planet import Planet
from classes.star import Star

WIDTH: Final = 800
HEIGHT: Final = 800
WINDOW: Final = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE: Final = "Universe Simulator"
pygame.display.set_caption(TITLE)

YELLOW: Final = (255, 255, 0)
BLUE: Final = (100, 149, 237)
RED: Final = (255, 0, 0)
DARK_GREY: Final = (80, 78, 81)
WHITE: Final = (255, 255, 255)

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Star(0, 0, 1.98892 * 10**30, YELLOW, 30, True)
    earth = Planet(-1 * Planet.AU, 0, 5.9742 * 10**24, BLUE, 16)
    mars = Planet(-1.524 * Planet.AU, 0, 6.39 * 10**23, RED, 12)
    mercury = Planet(0.387 * Planet.AU, 0, 3.30 * 10**23, DARK_GREY, 8)
    venus = Planet(0.723 * Planet.AU, 0, 4.8685 * 10**24, WHITE, 14) 


    used_celestial_bodies = (sun, earth, mars, mercury, venus)
    while run:
        clock.tick(60) # The loop will run at maximum 60 times per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for used_celestial_body in used_celestial_bodies:
            used_celestial_body.draw(WINDOW, WIDTH, HEIGHT)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
