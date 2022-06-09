from dis import dis
from typing import Final
import pygame
import numpy as np
from utils.calculate_attraction import calculate_attraction, calculate_distance
from utils.verify_calculation_by_sun import verify_calculation_by_sun

class CelestialBodies:
    AU: Final = np.array([149.6e6 * 1000])
    G: Final = np.array([6.67428e-11])
    TIMESTEP: Final = np.array([3600 * 24]) # 1 Day
    SCALE: Final = 100 / AU #1AU = 100 pixels

    def __init__(self, x: np.float32, y: np.float32, mass: np.ndarray, color, radius):
        self.x = x
        self.y = y
        self.mass = mass
        self.color = color
        self.radius = radius
        self.distance_from_sun = 0
        self.vector_distance = None
        self.orbit = []

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win, screen_width, screen_height, discover_sun, font):
        x = self.x * self.SCALE + screen_width / 2
        y = self.y * self.SCALE + screen_height / 2
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                w, z = point
                w = w * self.SCALE + screen_width / 2
                z = z * self.SCALE + screen_height / 2
                updated_points.append((w.item(), z.item()))
            pygame.draw.lines(win, self.color, False, updated_points, 2)
        
        pygame.draw.circle(win, self.color, (x.item(), y.item()), self.radius)
        if not discover_sun:
            distance_text = font.render(f"{self.distance_from_sun}m", 1, (255, 255, 255))
            win.blit(distance_text, (x.item() - distance_text.get_width()/2, y.item() - distance_text.get_height()/2 + 20))

    def update_position(self, celestial_bodies):
        total_fx = total_fy = 0
        for celestial_body in celestial_bodies:
            if self == celestial_body:
                continue
            distance, dx, dy = calculate_distance(self.x, self.y, celestial_body.x, celestial_body.y)
            verify_calculation_by_sun(self, celestial_body, distance)
            fx, fy = calculate_attraction(self.G, self.mass, celestial_body.mass, distance, dx, dy)
            total_fx = total_fx + fx 
            total_fy = total_fy + fy 

        self.x_vel = self.x_vel + total_fx / self.mass * self.TIMESTEP
        self.y_vel = self.y_vel + total_fy / self.mass * self.TIMESTEP

        self.x = self.x + self.x_vel * self.TIMESTEP
        self.y = self.y + self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

