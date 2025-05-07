from collections import deque

# Node class for A*
class Node:
    def __init__(self, pos, parent=None, g=0, h=0):
        self.pos = pos
        self.parent = parent
        self.g = g  # Cost from start
        self.h = h  # Heuristic (to goal)
        self.f = g + h  # Total cost

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_nodes = {start: Node(start, None, 0, manhattan(start, goal))}
    visited = set()
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # U, D, L, R

    while open_nodes:
        curr = min(open_nodes.values(), key=lambda n: n.f)
        del open_nodes[curr.pos]

        if curr.pos == goal:
            path = []
            while curr:
                path.append(curr.pos)
                curr = curr.parent
            return path[::-1]

        visited.add(curr.pos)

        for dx, dy in directions:
            r, c = curr.pos[0] + dx, curr.pos[1] + dy
            new_pos = (r, c)
            if 0 <= r < rows and 0 <= c < cols:
                if maze[r][c] != '#' and new_pos not in visited:
                    g = curr.g + 1
                    h = manhattan(new_pos, goal)
                    new_node = Node(new_pos, curr, g, h)
                    if new_pos not in open_nodes or open_nodes[new_pos].g > g:
                        open_nodes[new_pos] = new_node
    return None

# Maze grid
maze = [
    ['S', ' ', 'U', ' ', 'U', ' ', 'U', ' ', 'U', ' ', 'U', ' '],
    ['#', ' ', '#', ' ', 'U', ' ', '#', ' ', 'U', ' ', 'U', ' '],
    ['U', ' ', 'U', ' ', 'U', ' ', '+', ' ', 'U', ' ', 'U', ' '],
    ['U', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', 'U', ' '],
    ['U', ' ', 'U', ' ', '#', ' ', 'U', ' ', '#', ' ', 'G', ' ']
]

# Remove spaces for easier path tracking
maze = [[cell for cell in row if cell != ' '] for row in maze]

start = (0, 0)
goal = (4, 5)

# Run A*
path = a_star(maze, start, goal)

if path:
    for r, c in path:
        if (r, c) != start and (r, c) != goal:
            maze[r][c] = 'V'

    for row in maze:
        print(" ".join(row))
else:
    print("No path found.")

# Legend
print("\n-----------")
print("S -> Start\nG -> Goal\nV -> Path\nU -> Unvisited\n# -> Wall")

