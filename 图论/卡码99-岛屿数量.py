from collections import deque

n, m = map(int, input().split())

# 四个方向
position = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# 邻接矩阵
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
# 访问表
visited = [[False] * m for _ in range(n)]


def dfs(grid, visited, x, y):
    """
    深度优先搜索，对一整块陆地进行标记
    """
    for i, j in position:
        cur_x = x + i
        cur_y = y + j
        if cur_x < 0 or cur_x >= len(grid) or cur_y < 0 or cur_y >= len(grid[0]):
            continue
        if not visited[cur_x][cur_y] and grid[cur_x][cur_y] == 1:
            visited[cur_x][cur_y] = True
            dfs(grid, visited, cur_x, cur_y)


def bfs(grid, visited, x, y):
    """
    广度优先搜索对陆地进行标记
    """
    que = deque()
    que.append([x, y])
    while que:
        cur_x, cur_y = que.popleft()
        for i, j in position:
            next_x = cur_x + i
            next_y = cur_y + j
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                que.append([next_x, next_y])


# # dfs
# res = 0
# for i in range(n):
#     for j in range(m):
#         if grid[i][j] == 1 and not visited[i][j]:
#             res += 1
#             visited[i][j] = True
#             dfs(grid, visited, i, j)
#
# print(res)

# bfs
res = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            res += 1
            visited[i][j] = True
            bfs(grid, visited, i, j)

print(res)