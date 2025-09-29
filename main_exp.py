import numpy as np
import matplotlib.pyplot as plt

# Import the necessary solver functions
from problem import create_cities, calculate_distance_matrix
from hill_climbing_search import solve_with_hill_climbing
from tabu_search import solve_with_tabu_search

if __name__ == '__main__':
    # --- 1. Experiment Setup ---
    NUM_CITIES = 20
    NUM_RUNS = 30
    TABU_ITERATIONS = 500
    TABU_SIZE = 20

    # --- 2. Problem Creation ---
    # Create a single problem instance to be used for all runs
    cities = create_cities(NUM_CITIES)
    dist_matrix = calculate_distance_matrix(cities)

    # --- 3. Main Experiment: Hill Climbing vs. Tabu Search ---
    print(f"--- Starting experiment ({NUM_CITIES} cities, {NUM_RUNS} runs) ---")
    hc_results = []
    ts_results = []

    for i in range(NUM_RUNS):
        print(f"Run {i+1}/{NUM_RUNS}...")
        
        # Hill Climbing
        # The history return value is not needed here, so we use _
        _, hc_dist, _ = solve_with_hill_climbing(dist_matrix)
        hc_results.append(hc_dist)
        
        # Tabu Search
        _, ts_dist, _ = solve_with_tabu_search(dist_matrix, 
                                             iterations=TABU_ITERATIONS, 
                                             tabu_size=TABU_SIZE)
        ts_results.append(ts_dist)

    # --- 4. Statistical Summary ---
    print("\n--- Experiment Results Summary ---")
    hc_results = np.array(hc_results)
    ts_results = np.array(ts_results)

    print("\n[Hill Climbing]")
    print(f"Average Distance: {hc_results.mean():.2f}")
    print(f"Standard Deviation: {hc_results.std():.2f}")
    print(f"Best Distance Found: {hc_results.min():.2f}")

    print("\n[Tabu Search]")
    print(f"Average Distance: {ts_results.mean():.2f}")
    print(f"Standard Deviation: {ts_results.std():.2f}")
    print(f"Best Distance Found: {ts_results.min():.2f}")
    
    run_numbers = range(1, NUM_RUNS + 1)

    plt.figure(figsize=(12, 8))
    plt.plot(run_numbers, hc_results, label='Hill Climbing', color='orange', marker='o', linestyle='--')
    plt.plot(run_numbers, ts_results, label='Tabu Search', color='blue', marker='x', linestyle='-')
    
    plt.title(f'Performance Consistency ({NUM_CITIES} Cities over {NUM_RUNS} Runs)')
    plt.xlabel('Run Number')
    plt.ylabel('Final Total Distance')
    
    plt.xticks(np.arange(min(run_numbers), max(run_numbers)+1, step=2.0))
    
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()