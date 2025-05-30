
from collections import deque

def bfs_shortest_path(graph, start, target):
    visited = set()
    queue = deque([(start, [start])])  # Store the path along with the node
    
    while queue:
        vertex, path = queue.popleft()
        if vertex == target:
            return path  # Return the path when target is found
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

shortest_path = bfs_shortest_path(graph, 'A', 'F')
print(f"Shortest path from A to F: {' -> '.join(shortest_path)}")

