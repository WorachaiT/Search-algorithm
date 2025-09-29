import numpy as np
import time
from problem import create_cities, calculate_distance_matrix, calculate_total_distance

def get_hc_neighbors(route):
    """Generates neighbors for Hill Climbing by swapping two cities."""
    neighbors = []
    num_cities = len(route)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            neighbor = route.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def solve_with_hill_climbing(dist_matrix):
    """Solves TSP using Hill Climbing."""
    num_cities = len(dist_matrix)
    current_route = list(np.random.permutation(num_cities))
    current_dist = calculate_total_distance(current_route, dist_matrix)
    history = [current_dist]

    while True:
        neighbors = get_hc_neighbors(current_route)
        best_neighbor = None
        best_neighbor_dist = current_dist
        for neighbor in neighbors:
            dist = calculate_total_distance(neighbor, dist_matrix)
            if dist < best_neighbor_dist:
                best_neighbor = neighbor
                best_neighbor_dist = dist
        
        if best_neighbor is None:
            break
        
        current_route = best_neighbor
        current_dist = best_neighbor_dist
        history.append(current_dist)
        
    return current_route, current_dist, history

# This block allows the file to be run directly for testing.
if __name__ == '__main__':
    NUM_CITIES_TEST = 20
    
    print(f"--- Test for Hill Climbing with {NUM_CITIES_TEST} cities ---")
    
    test_cities = create_cities(NUM_CITIES_TEST)
    test_dist_matrix = calculate_distance_matrix(test_cities)
    print(f"Problem created with {len(test_cities)} cities.")
    
    print("Solving...")
    start_time = time.time()
    # We don't need the history for this simple test, so we use _
    best_route, best_distance, _ = solve_with_hill_climbing(test_dist_matrix)
    end_time = time.time()
    
    print("\n--- Hill Climbing Test Results ---")
    print(f"Best distance found: {best_distance:.2f}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")