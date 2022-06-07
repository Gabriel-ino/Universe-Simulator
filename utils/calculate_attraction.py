import numpy as np
from numba import jit

@jit(nopython=True, parallel=True)
def calculate_distance(first_coordinates: np.ndarray, second_coordinates: np.ndarray):
    distance_x = np.float32(second_coordinates[0] - first_coordinates[0])
    distance_y = np.float32(second_coordinates[1] - first_coordinates[1])
    distance_array = np.array([distance_x ** 2 + distance_y ** 2])
    distance = np.sqrt(distance_array)
    return distance, np.array([distance_x, distance_y])
    

@jit(nopython=True, parallel=True)
def calculate_attraction(first_elements: np.ndarray, second_mass: np.float32, distance: np.float32):
    force = first_elements[0] * first_elements[1] * second_mass / distance ** 2

