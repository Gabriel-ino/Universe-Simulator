from typing import Final
import pygame

class CelestialBodies:
    AU: Final = 149.6e6 * 1000
    G: Final = 6.67428e-11
    TIMESTEP: Final = 3600 * 24 # 1 Day
    SCALE: Final = 250 / AU #1AU = 100 pixels

    def __init__(self, x, y, mass, color, radius):
        self.x = x
        self.y = y
        self.mass = mass
        self.color = color
        self.radius = radius
        self.orbit = None

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win, screen_width, screen_height):
        x = self.x * self.SCALE + screen_width / 2
        y = self.y * self.SCALE + screen_height / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius) 

