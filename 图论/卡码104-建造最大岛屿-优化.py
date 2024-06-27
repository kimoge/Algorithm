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


def dfs(grid, x, y, visited, mark):
    """
    深度优先搜索，给每个岛屿加上标记
    """
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return 
    if visited[x][y] or grid[x][y] == 0:
        return

    visited[x][y] = True
    grid[x][y] = mark
    count[0] += 1
    
    for i, j in position:
        cur_x = x + i
        cur_y = y + j
        dfs(grid, cur_x, cur_y, visited, mark)



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

dic = dict()
mark = 2
flag = True
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            count[0] = 0
            dfs(grid, i, j, visited, mark)
            dic[mark] = count[0]
            mark += 1
        if grid[i][j] == 0:
            flag = False

if flag:
    print(n * m)
else:
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                cur_res = 1
                s = set()
                for p, q in position:
                    cur_x = p + i
                    cur_y = q + j
                    if cur_x < 0 or cur_x >= len(grid) or cur_y < 0 or cur_y >= len(grid[0]):
                        continue
                    if grid[cur_x][cur_y] == 0:
                        continue
                    if grid[cur_x][cur_y] in s:
                        continue
                    s.add(grid[cur_x][cur_y])
                    cur_res += dic[grid[cur_x][cur_y]]
                res = max(res, cur_res)
    print(res)



