
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_with_path(self, start, path=None):
        if path is None:
            path = []
        path.append(start)
        for neighbor in self.graph.get(start, []):
            if neighbor not in path:
                self.dfs_with_path(neighbor, path)
        return path

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("\nDFS with Path Tracking:")
result_path = g.dfs_with_path(0)
print("Path:", result_path)
