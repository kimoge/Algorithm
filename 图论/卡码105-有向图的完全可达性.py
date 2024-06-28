from collections import deque
n, k = map(int, input().split())

# 四个方向
position = [[0, 1], [1, 0], [0, -1], [-1, 0]]
grid = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(k):
    s, t = map(int, input().split())
    grid[s][t] = 1

visited = [False] * (n + 1)
visited[0] = True


def dfs(grid, visited, key):
    """
    深度优先搜索，访问当前节点，找下一个可达节点递归访问
    """
    if visited[key]:
        return

    visited[key] = True
    for i in range(1, n+1):
        if grid[key][i] == 1:
            dfs(grid, visited, i)


def bfs(grid, visited, key):
    queue = deque()
    queue.append(key)
    visited[key] = True
    while queue:
        cur_key = queue.popleft()
        for i in range(1, n+1):
            if not visited[i] and grid[cur_key][i] == 1:
                queue.append(i)
                visited[i] = True



bfs(grid, visited, 1)

flag = True
for i in visited[1:]:
    if not i:
        flag = i
        break
if flag:
    print(1)
else:
    print(-1)
