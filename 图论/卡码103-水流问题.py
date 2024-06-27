from collections import deque

n, m = map(int, input().split())
# 四个方向
position = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# 邻接矩阵
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
# print(grid)
visited_first = [[False] * m for _ in range(n)]
visited_second = [[False] * m for _ in range(n)]


def dfs(grid, x, y, visited):
    """
    深度优先搜索
    """
    for i, j in position:
        cur_x = x + i
        cur_y = y + j
        if cur_x < 0 or cur_x >= len(grid) or cur_y < 0 or cur_y >= len(grid[0]):
            continue
        if grid[cur_x][cur_y] < grid[x][y] or visited[cur_x][cur_y]:
            continue
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


for i in range(n):
    if not visited_first[i][0]:
        visited_first[i][0] = True
        dfs(grid, i, 0, visited_first)
    if not visited_second[i][m-1]:
        visited_second[i][m-1] = True
        dfs(grid, i, m-1, visited_second)

for i in range(m):
    if not visited_first[0][i]:
        visited_first[0][i] = True
        dfs(grid, 0, i, visited_first)
    if not visited_second[n-1][i]:
        visited_second[n-1][i] = True
        dfs(grid, n-1, i, visited_second)


for i in range(n):
    for j in range(m):
        if visited_first[i][j] and visited_second[i][j]:
            print(i, j)