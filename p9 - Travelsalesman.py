
import itertools

def calculate_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to starting city
    return total_distance

def tsp_brute_force(distance_matrix):
    cities = list(range(len(distance_matrix)))
    min_distance = float('inf')
    best_route = None
    
    for perm in itertools.permutations(cities):
        current_distance = calculate_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = perm
            
    return best_route, min_distance

# Example usage
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
route, distance = tsp_brute_force(distance_matrix)
print("Best route:", route, "with distance:", distance)
