import numpy as np
from typing import Final
from .celestial_bodies import CelestialBodies


class Planet(CelestialBodies):
    def __init__(self,x, y, mass, color, radius):
        super().__init__(x, y, mass, color, radius)
        self.distance_from_sun = 0 



