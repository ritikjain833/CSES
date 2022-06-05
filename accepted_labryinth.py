 
import sys
from collections import deque
rows, cols = [int(s) for s in sys.stdin.readline().split()]
grid = [[0 for _ in range(cols)] for _ in range(rows)]
source, dest = None, None
for row in range(rows):
    for col, ch in enumerate(sys.stdin.readline().strip()):
        if ch == 'A':
            source = (row, col)
        elif ch == 'B':
            dest = (row, col)
        grid[row][col] = ch
 
 
dx = [-1, 0, 1, 0]  # left, top, right, bottom
dy = [0, -1, 0, 1]
 
 
def bfs(grid, source, dest):
    queue = deque([source])
    parents = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
    parents[source[0]][source[1]] = -1
    while queue:
        node = queue.popleft()
        # print(node, dest)
        if node == dest:
            print("YES")
            path = []
            while parents[node[0]][node[1]] != -1:
                prev_ = parents[node[0]][node[1]]
                if prev_[0] - node[0] > 0:
                    path.append("U")
                elif prev_[0] - node[0] < 0:
                    path.append("D")
                elif prev_[1] - node[1] > 0:
                    path.append("L")
                elif prev_[1] - node[1] < 0:
                    path.append("R")
                node = prev_
            print(len(path))
            print("".join((s for s in reversed(path))))
            return
        for i in range(len(dx)):
            n_row = node[0] + dx[i] 
            n_col = node[1] + dy[i]
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]) and grid[n_row][n_col] != '#' and parents[n_row][n_col] is None:
                parents[n_row][n_col] = node
                queue.append((n_row, n_col))
    print("NO")
 
 
bfs(grid, source, dest)