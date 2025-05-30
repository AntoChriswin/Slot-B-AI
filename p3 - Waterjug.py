from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    q = deque()
    q.append((0, 0))
    while q:
        a, b = q.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        print(f"Jug1: {a}L, Jug2: {b}L")

        if a == target or b == target or a + b == target:
            print("Target reached!")
            return True

        
        states = [
            (jug1, b),        
            (a, jug2),        
            (0, b),          
            (a, 0),           
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),  
            (a + min(b, jug1 - a), b - min(b, jug1 - a))           ]

        for state in states:
            if state not in visited:
                q.append(state)

    print("No solution.")
    return False
