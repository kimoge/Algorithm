# 提示：岛屿周围为0or超出边界时周长 +1
import sys
from collections import deque
n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
# print(grid)
# 四个方向
position = [[0, 1], [1, 0], [0, -1], [-1, 0]]
length = [0]


def dfs(grid, visited, x, y):
    visited[x][y] = True
    for i, j in position:
        next_x = x + i
        next_y = y + j
        # 当超出边界时 周长+1
        if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
            length[0] += 1
            continue
        # 当下一个节点是海时 周长+1
        if grid[next_x][next_y] == 0:
            length[0] += 1
            continue
        if visited[next_x][next_y]:
            continue
        dfs(grid, visited, next_x, next_y)


def bfs(grid, visited, x, y):
    que = deque()
    visited[x][y] = True
    que.append([x, y])
    while que:
        cur_x, cur_y = que.popleft()
        for i, j in position:
            next_x = cur_x + i
            next_y = cur_y + j
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                length[0] += 1
                continue
            # 当下一个节点是海时 周长+1
            if grid[next_x][next_y] == 0:
                length[0] += 1
                continue
            if visited[next_x][next_y]:
                continue

            visited[next_x][next_y] = True
            que.append([next_x, next_y])


for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            # dfs(grid, visited, i, j)
            bfs(grid, visited, i, j)
            print(length[0])
            sys.exit()