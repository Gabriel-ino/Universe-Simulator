import pygame
from typing import Final
import numpy as np
from classes.planet import Planet
from classes.star import Star
from functools import lru_cache


@lru_cache
def discover_sun(obj):
    verifier = isinstance(obj, Star)
    if verifier:
        verifier = obj.is_the_sun
    return verifier

pygame.init()


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

FONT: Final = pygame.font.SysFont('comicsans', 16)


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Star(np.float32(0), np.float32(0), np.float32(1.98892 * 10**30), YELLOW, 30, True)

    earth = Planet(np.float32(-1 * Planet.AU), np.float32(0), np.float32(5.9742 * 10**24), BLUE, 16)
    earth.y_vel = np.array([29.783 * 1000])

    mars = Planet(np.float32(-1.524 * Planet.AU), np.float32(0), np.float32(6.39 * 10**23), RED, 12)
    mars.y_vel = np.array([24.077 * 1000])

    mercury = Planet(np.float32(0.387 * Planet.AU), np.float32(0), np.float32(3.30 * 10**23), DARK_GREY, 8)
    mercury.y_vel = np.array([47.4 * 1000])

    venus = Planet(np.float32(0.723 * Planet.AU), np.float32(0), np.float32(4.8685 * 10**24), WHITE, 14)
    venus.y_vel = np.array([-35.02 * 1000])

    used_celestial_bodies = (sun, earth, mars, mercury, venus)
    while run:
        clock.tick(60) # The loop will run at maximum 60 times per second
        WINDOW.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for used_celestial_body in used_celestial_bodies:
            used_celestial_body.update_position(used_celestial_bodies)
            used_celestial_body.draw(WINDOW, WIDTH, HEIGHT, discover_sun(used_celestial_body), FONT)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
