from .celestial_bodies import CelestialBodies

class Star(CelestialBodies):
    def __init__(self, x, y, radius, color, mass, is_the_sun):
        super().__init__(x, y, radius, color, mass)
        self.is_the_sun = is_the_sun
