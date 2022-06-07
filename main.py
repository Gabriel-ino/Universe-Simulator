import pygame
from typing import Final
import numpy as np
from classes.planet import Planet
from classes.star import Star
from utils.calculate_attraction import calculate_distance
from functools import lru_cache

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

@lru_cache
def verify_calculation_by_sun(celestial_body1, celestial_body2, distance):
    try:
        verifier = celestial_body2.is_the_sun
    except not isinstance(celestial_body2, Star):
        return False

    if verifier:
        celestial_body1.distance_from_sun = distance
    return True
    


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Star(np.float32(0), np.float32(0), np.float32(1.98892 * 10**30), YELLOW, 30, True)
    earth = Planet(np.float32(-1 * Planet.AU), np.float32(0), np.float32(5.9742 * 10**24), BLUE, 16)
    mars = Planet(np.float32(-1.524 * Planet.AU), np.float32(0), np.float32(6.39 * 10**23), RED, 12)
    mercury = Planet(np.float32(0.387 * Planet.AU), np.float32(0), np.float32(3.30 * 10**23), DARK_GREY, 8)
    venus = Planet(np.float32(0.723 * Planet.AU), np.float32(0), np.float32(4.8685 * 10**24), WHITE, 14)

    calculate_distance(np.array([earth.x, earth.y]), np.array([sun.x, sun.y])) 


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
