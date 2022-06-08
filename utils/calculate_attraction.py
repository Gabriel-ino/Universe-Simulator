import numpy as np
from numba import jit

@jit(nopython=True, parallel=True)
def calculate_distance(p1x: np.ndarray, p1y: np.ndarray, p2x: np.ndarray, p2y: np.ndarray):
    distance_x = p2x - p1x
    distance_y = p2y - p1y
    distance_array = distance_x ** 2 + distance_y ** 2
    distance = np.sqrt(distance_array)
    
    return distance, distance_x, distance_y
    

@jit(parallel=True)
def calculate_attraction(gravity: np.ndarray, mass: np.ndarray, second_mass: np.float32, distance: np.ndarray, distance_x: np.ndarray, distance_y: np.ndarray):
    force = gravity * mass * second_mass.item() / distance ** 2
    theta = np.arctan2(distance_y, distance_x)
    force_x = np.cos(theta) * force
    force_y = np.sin(theta) * force
    return force_x, force_y

