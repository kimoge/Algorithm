# dijkstra求解最短路径, 时间复杂度 n^2
n, m = map(int, input().split())
max_int = 1000

start = 1  # 起点
end = n  # 终点
grid = [[max_int] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    s, e, v = map(int, input().split())
    grid[s][e] = v

minDist = [max_int] * (n + 1)
visited = [False] * (n + 1)
minDist[start] = 0

parent = [-1] * (n + 1)  # 记录最短路径
for _ in range(n):
    # 1、根据minDist选择要加入的节点
    cur = -1
    minVal = max_int
    for i in range(1, n + 1):
        if minVal > minDist[i] and not visited[i]:
            minVal = minDist[i]
            cur = i

    # 2、加入节点，更新visited表
    visited[cur] = True

    # 3、更新minDist表
    for i in range(1, n + 1):
        if not visited[i] and grid[cur][i] != max_int and minDist[cur] + grid[cur][i] < minDist[i]:
            minDist[i] = minDist[cur] + grid[cur][i]
            parent[i] = cur
# print(minDist)
# if minDist[end] == max_int:
#     print(-1)
# else:
#     print(minDist[end])

# 打印最短路径
# print(parent)
for i in range(1, n + 1):
    print(parent[i], "->", i)