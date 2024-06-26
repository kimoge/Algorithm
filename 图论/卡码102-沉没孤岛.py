# 大致思路：设置函数遍历陆地过后将其值标记为2，对四周调用，再对所有陆地值-1就可以了
from collections import deque

n, m = map(int, input().split())

# 四个方向
position = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# 邻接矩阵
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))


def dfs(grid, x, y):
    """
    深度优先搜索，对一整块陆地进行标记
    """
    grid[x][y] = 2
    for i, j in position:
        cur_x = x + i
        cur_y = y + j
        if cur_x < 0 or cur_x >= len(grid) or cur_y < 0 or cur_y >= len(grid[0]):
            continue
        if grid[cur_x][cur_y] == 0 or grid[cur_x][cur_y] == 2:
            continue

        dfs(grid, cur_x, cur_y)


def bfs(grid, x, y):
    """
    广度优先搜索对陆地进行标记
    """
    que = deque()
    que.append([x, y])
    grid[x][y] = 2
    while que:
        cur_x, cur_y = que.popleft()
        for i, j in position:
            next_x = cur_x + i
            next_y = cur_y + j
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            if grid[next_x][next_y] == 1:
                que.append([next_x, next_y])
                grid[next_x][next_y] = 2


# # dfs
# for i in range(n):
#     if grid[i][0] == 1:
#         dfs(grid, i, 0)
#     if grid[i][m-1] == 1:
#         dfs(grid, i, m-1)
#
# for i in range(m):
#     if grid[0][i] == 1:
#         dfs(grid, 0, i)
#     if grid[n-1][i] == 1:
#         dfs(grid, n - 1, i)
#
# for i in range(n):
#     for j in range(m):
#         if grid[i][j] != 0:
#             grid[i][j] -= 1
#
# # print(grid)
# for i in grid:
#     for j in i:
#         print(j, end=" ")
#     print()

# bfs
for i in range(n):
    if grid[i][0] == 1:
        bfs(grid, i, 0)
    if grid[i][m-1] == 1:
        bfs(grid, i, m-1)

for i in range(m):
    if grid[0][i] == 1:
        bfs(grid, 0, i)
    if grid[n-1][i] == 1:
        bfs(grid, n - 1, i)

for i in range(n):
    for j in range(m):
        if grid[i][j] != 0:
            grid[i][j] -= 1

for i in grid:
    for j in i:
        print(j, end=" ")
    print()