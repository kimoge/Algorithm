# 时间复杂度 eloge

import heapq
n, m = map(int, input().split())
max_int = 1000

start = 1  # 起点
end = n  # 终点

# 邻接表
grid = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, v = map(int, input().split())
    grid[s].append([v, e]) # 值，结点

minDist = [max_int] * (n + 1)
visited = [False] * (n + 1)
minDist[start] = 0

# 优先队列构造小顶堆
pri_que = []
heapq.heappush(pri_que, [0, start])

while pri_que:
    cur = heapq.heappop(pri_que)
    if visited[cur[1]]:
       continue

    visited[cur[1]] = True

    for v, e in grid[cur[1]]:
        # v:当前节点cur[1]到节点e的消耗    cur[0]:从起点到cur[1]的消耗
        if not visited[e] and v + cur[0] < minDist[e]:
            minDist[e] = v + cur[0]
            heapq.heappush(pri_que, [minDist[e], e])

if minDist[end] == max_int:
    print(-1)
else:
    print(minDist[end])
