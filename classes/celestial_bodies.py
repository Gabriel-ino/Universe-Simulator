from typing import Final
import pygame
import numpy as np

class CelestialBodies:
    AU: Final = np.float32(149.6e6 * 1000)
    G: Final = np.float32(6.67428e-11)
    TIMESTEP: Final = np.float32(3600 * 24) # 1 Day
    SCALE: Final = 250 / AU #1AU = 100 pixels

    def __init__(self, x: np.float32, y: np.float32, mass: np.float32, color, radius):
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

