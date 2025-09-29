import collections
import time
from problem import create_cities, calculate_distance_matrix, calculate_total_distance

def solve_tsp_with_bfs(dist_matrix):
    """Solves TSP using a brute-force BFS approach (cleaner version)."""
    num_cities = len(dist_matrix)
    # The state in the queue now only stores the path.
    queue = collections.deque([ (0,) ]) # Start with a path containing only city 0
    completed_tours = []

    while queue:
        path = queue.popleft() # We only get the path now.

        if len(path) == num_cities:
            completed_tours.append(list(path))
            continue

        # Find the next possible cities to visit
        for next_city in range(num_cities):
            if next_city not in path:
                new_path = path + (next_city,)
                queue.append(new_path)
    
    # After finding all possible tours, find the best one.
    best_dist = float('inf')
    best_route = None
    for route in completed_tours:
        dist = calculate_total_distance(route, dist_matrix)
        if dist < best_dist:
            best_dist = dist
            best_route = route
            
    return best_route, best_dist

# This block allows the file to be run directly for testing.
if __name__ == '__main__':
    NUM_CITIES_TEST = 12
    print(f"--- Standalone Test for BFS with {NUM_CITIES_TEST} cities ---")
    
    test_cities = create_cities(NUM_CITIES_TEST)
    test_dist_matrix = calculate_distance_matrix(test_cities)
    print(f"Problem created with {len(test_cities)} cities.")
    
    print("Solving...")
    start_time = time.time()
    best_route, best_distance = solve_tsp_with_bfs(test_dist_matrix)
    end_time = time.time()
    
    print("\n--- BFS Test Results ---")
    print(f"Best route found: {best_route}")
    print(f"Best distance: {best_distance:.2f}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
