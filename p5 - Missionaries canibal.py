
from collections import deque

# Define the state as (M_left, C_left, Boat_side)
# Boat_side: 0 = left bank, 1 = right bank

def is_valid(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left and m_left < c_left:
        return False
    if m_right and m_right < c_right:
        return False
    return True

def get_successors(state):
    m, c, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    successors = []

    for dm, dc in moves:
        if boat == 0:  # Boat on left
            new_m, new_c = m - dm, c - dc
            m_right, c_right = 3 - new_m, 3 - new_c
            if is_valid(new_m, new_c, m_right, c_right):
                successors.append((new_m, new_c, 1))
        else:  # Boat on right
            new_m, new_c = m + dm, c + dc
            m_right, c_right = 3 - new_m, 3 - new_c
            if is_valid(new_m, new_c, m_right, c_right):
                successors.append((new_m, new_c, 0))
    return successors

def bfs():
    start = (3, 3, 0)
    goal = (0, 0, 1)
    visited = set()
    queue = deque()
    queue.append((start, [start]))

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    return None

# Run the solution
solution = bfs()

if solution:
    print("Solution found! Steps:")
    for step in solution:
        print(f"Left Bank -> M: {step[0]} C: {step[1]}, Boat: {'Left' if step[2]==0 else 'Right'}")
else:
    print("No solution found.")
