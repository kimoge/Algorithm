# 求最短路径 + 路径权值出现负数时 使用Bellman-ford队列优化算法（即SPFA算法）
# 与Bellman-ford相比，SPFA使用队列记录上一次松弛的节点，以便更新与其相邻的边的路径值
from collections import deque

n, m = map(int, input().split())
max_int = 101
# 使用邻接表
grid = [[] for _ in range(n+1)]
for _ in range(m):
    s, t, v = map(int, input().split())
    grid[s].append([t, v])

start = 1  # 起点
end = n  # 终点

minDist = [max_int] * (n + 1)
minDist[start] = 0  # 初始化起点最短距离

que = deque()
que.append(start)
while que:
    cur_s = que.popleft()
    for cur_t, cur_v in grid[cur_s]:
        if minDist[cur_s] + cur_v < minDist[cur_t]:
            minDist[cur_t] = minDist[cur_s] + cur_v
            que.append(cur_t)

if minDist[end] != max_int:
    print(minDist[end])
else:
    print("unconnected")