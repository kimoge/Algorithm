# 思路：找到水的一格向外搜索陆地
from collections import deque

n, m = map(int, input().split())
# 四个方向
position = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# 邻接矩阵
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
# print(grid)
count = [1]


def dfs(grid, x, y, visited):
    """
    深度优先搜索
    """
    for i, j in position:
        cur_x = x + i
        cur_y = y + j
        if cur_x < 0 or cur_x >= len(grid) or cur_y < 0 or cur_y >= len(grid[0]):
            continue
        if grid[cur_x][cur_y] == 0 or visited[cur_x][cur_y]:
            continue
        count[0] += 1
        visited[cur_x][cur_y] = True
        dfs(grid, cur_x, cur_y, visited)



def bfs(grid, x, y):
    """
    广度优先搜索对陆地进行标记
    """
    que = deque()
    que.append([x, y])
    grid[x][y] = 0
    while que:
        cur_x, cur_y = que.popleft()
        for i, j in position:
            next_x = cur_x + i
            next_y = cur_y + j
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            if grid[next_x][next_y] == 1:
                que.append([next_x, next_y])
                grid[next_x][next_y] = 0


res = 1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            count[0] = 1
            visited = [[False] * m for _ in range(n)]
            dfs(grid, i, j, visited)
            res = max(res, count[0])
        else:
            count[0] = 1
            visited = [[False] * m for _ in range(n)]
            visited[i][j] = True
            dfs(grid, i, j, visited)
            res = max(res, count[0])
print(res)
