import numpy as np

def create_cities(num_cities, width=100, height=100):
    """Creates random city coordinates in a given space."""
    return np.random.rand(num_cities, 2) * [width, height]

def calculate_distance_matrix(cities):
    """Calculates the distance matrix for all pairs of cities."""
    num_cities = cities.shape[0]
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            # Calculate Euclidean distance
            dist = np.linalg.norm(cities[i] - cities[j])
            dist_matrix[i, j] = dist_matrix[j, i] = dist
    return dist_matrix

def calculate_total_distance(route, dist_matrix):
    """Calculates the total distance of a given route."""
    total_dist = 0
    num_cities = len(route)
    for i in range(num_cities):
        # Distance from the current city to the next (looping back to start)
        total_dist += dist_matrix[route[i], route[(i + 1) % num_cities]]
    return total_dist
