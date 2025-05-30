
class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.position = (0, 0)  # Starting position
        self.cleaned = 0

    def clean(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:  # 1 represents dirty
                    self.cleaned += 1
                    self.grid[i][j] = 0  # Clean the spot
                    print(f"Cleaned position: ({i}, {j})")

    def get_cleaned_count(self):
        return self.cleaned

# Example usage
grid = [[0, 1, 0], [1, 1, 0], [0, 0, 1]]
vacuum = VacuumCleaner(grid)
vacuum.clean()
print(f"Total cleaned spots: {vacuum.get_cleaned_count()}")
