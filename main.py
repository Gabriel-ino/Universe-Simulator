import pygame
from typing import Final
import numpy as np
from classes.planet import Planet
from classes.star import Star
from classes.button import Button
from functools import lru_cache


@lru_cache
def discover_sun(obj):
    verifier = isinstance(obj, Star)
    if verifier:
        verifier = obj.is_the_sun
    return verifier

@lru_cache
def verify_mouse_on_top(x, y, mouse):
    if x/2 <= mouse[0] <= x/2 + 140 and y/2 <= mouse[1] <= y/2 + 40:
        return True
    return False


pygame.init()

FONT: Final = pygame.font.SysFont('comicsans', 16)
BUTTON_FONT: Final = pygame.font.SysFont('comicsans', 32)
YELLOW: Final = (255, 255, 0)
BLUE: Final = (100, 149, 237)
RED: Final = (255, 0, 0)
DARK_GREY: Final = (80, 78, 81)
WHITE: Final = (255, 255, 255)
PASTEL: Final = (249, 234, 195)
VIOLET_BLUE: Final = (148, 119, 252)
CYAN: Final = (0, 255, 255)

WIDTH: Final = 1400
HEIGHT: Final = 800
WINDOW: Final = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE: Final = "Universe Simulator"
pygame.display.set_caption(TITLE)

LOADING: Final = FONT.render("Loading, please wait...", 15, WHITE)
WINDOW.blit(LOADING, (WIDTH/2, HEIGHT/2))
pygame.display.update()



def main():
    run = True
    clock = pygame.time.Clock()

    sun = Star("Sun", np.float32(0), np.float32(0), np.float32(1.98892 * 10**30), YELLOW, 30, True)

    earth = Planet("Earth", np.float32(-1 * Planet.AU), np.float32(0), np.float32(5.9742 * 10**24), BLUE, 16)
    earth.y_vel = np.array([29.783 * 1000])

    mars = Planet("Mars", np.float32(-1.524 * Planet.AU), np.float32(0), np.float32(6.39 * 10**23), RED, 12)
    mars.y_vel = np.array([24.077 * 1000])

    mercury = Planet("Mercury", np.float32(0.387 * Planet.AU), np.float32(0), np.float32(3.30 * 10**23), DARK_GREY, 8)
    mercury.y_vel = np.array([47.4 * 1000])

    venus = Planet("Venus", np.float32(0.723 * Planet.AU), np.float32(0), np.float32(4.8685 * 10**24), WHITE, 14)
    venus.y_vel = np.array([-35.02 * 1000])

    jupiter = Planet("Jupiter", np.float32(5.2028 * Planet.AU), np.float32(0), np.float32(1.9 * 10**27), PASTEL, 20)
    jupiter.y_vel = np.array([13.07 * 1000])

    neptune = Planet("Neptune", np.float32(30.0611 * Planet.AU), np.float32(0), np.float32(1.024 * 10**26), VIOLET_BLUE, 18)
    neptune.y_vel = np.array([5.45 * 1000])

    uranus = Planet("Uranus", np.float32(19.1914 * Planet.AU), np.float32(0), np.float32(8.686 * 10**25), CYAN, 19)
    uranus.y_vel = np.array([6.81 * 1000])

    close_button = Button(10, 30, (170, 170, 170), (100, 100, 100), BUTTON_FONT, "Close")



    used_celestial_bodies = (sun, earth, mars, mercury, venus, jupiter, neptune, uranus)
    while run:
        clock.tick(60) # The loop will run at maximum 60 times per second
        WINDOW.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.pos_x / 2 <= mouse[0] <= close_button.pos_x / 2 + 140 and close_button.pos_y /2 <= mouse[1] <= close_button.pos_y / 2 + 40:
                    run = False

        mouse = pygame.mouse.get_pos()
        close_button.draw(WINDOW, verify_mouse_on_top(close_button.pos_x, close_button.pos_y, mouse))
        for used_celestial_body in used_celestial_bodies:
            used_celestial_body.update_position(used_celestial_bodies)
            used_celestial_body.draw(WINDOW, WIDTH, HEIGHT, discover_sun(used_celestial_body), FONT)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
