def is_safe(graph, color, node, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def map_coloring_util(graph, m, color, node):
    if node == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, color, node, c):
            color[node] = c
            if map_coloring_util(graph, m, color, node + 1):
                return True
            color[node] = 0  # Backtrack
    return False

def map_coloring(graph, m):
    color = [0] * len(graph)
    if map_coloring_util(graph, m, color, 0):
        return color
    return None

# Example usage
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1]
}
m = 3  # Number of colors
result = map_coloring(graph, m)
print("Coloring of the map:", result)
