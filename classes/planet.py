import numpy as np
from typing import Final
from .celestial_bodies import CelestialBodies


class Planet(CelestialBodies):
    def __init__(self,name, x, y, mass, color, radius):
        super().__init__(name, x, y, mass, color, radius)
        self.istheEarth = False
        if self.name == 'Earth':
            self.istheEarth = True

