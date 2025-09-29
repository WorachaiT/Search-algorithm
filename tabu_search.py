import numpy as np
import collections
import time
from problem import create_cities, calculate_distance_matrix, calculate_total_distance

def get_ts_neighbors(route):
    """Generates neighbors and the 'move' for Tabu Search."""
    neighbors_with_moves = []
    num_cities = len(route)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            neighbor = route.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            move = tuple(sorted((route[i], route[j])))
            neighbors_with_moves.append((neighbor, move))
    return neighbors_with_moves

def solve_with_tabu_search(dist_matrix, iterations=500, tabu_size=20):
    """Solves TSP using Tabu Search."""
    num_cities = len(dist_matrix)
    current_route = list(np.random.permutation(num_cities))
    best_route = current_route
    best_dist = calculate_total_distance(best_route, dist_matrix)
    
    tabu_list = collections.deque(maxlen=tabu_size)
    history = [best_dist]

    for _ in range(iterations):
        neighbors_with_moves = get_ts_neighbors(current_route)
        best_neighbor = None
        best_neighbor_dist = float('inf')
        best_move = None
        
        for neighbor, move in neighbors_with_moves:
            if move not in tabu_list:
                dist = calculate_total_distance(neighbor, dist_matrix)
                if dist < best_neighbor_dist:
                    best_neighbor = neighbor
                    best_neighbor_dist = dist
                    best_move = move
        
        if best_neighbor is None:
            continue
            
        current_route = best_neighbor
        if best_move:
            tabu_list.append(best_move)
        
        if best_neighbor_dist < best_dist:
            best_route = best_neighbor
            best_dist = best_neighbor_dist
        
        history.append(best_dist)
            
    return best_route, best_dist, history

# This block allows the file to be run directly for testing.
if __name__ == '__main__':
    NUM_CITIES_TEST = 20
    ITERATIONS_TEST = 500
    TABU_SIZE_TEST = 20
    
    print(f"--- Test for Tabu Search with {NUM_CITIES_TEST} cities ---")
    
    test_cities = create_cities(NUM_CITIES_TEST)
    test_dist_matrix = calculate_distance_matrix(test_cities)
    print(f"Problem created with {len(test_cities)} cities.")
    
    print("Solving...")
    start_time = time.time()
    # We don't need the history for this simple test, so we use _
    best_route, best_distance, _ = solve_with_tabu_search(
        test_dist_matrix, 
        iterations=ITERATIONS_TEST, 
        tabu_size=TABU_SIZE_TEST
    )
    end_time = time.time()
    
    print("\n--- Tabu Search Test Results ---")
    print(f"Best distance found: {best_distance:.2f}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")