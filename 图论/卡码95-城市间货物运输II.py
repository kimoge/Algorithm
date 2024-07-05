# 与I相比，此次有可能有负权回路
from collections import deque
n, m = map(int, input().split())
max_int = 101
start = 1  # 起点
end = n  # 终点
minDist = [max_int] * (n + 1)
minDist[start] = 0  # 初始化起点最短距离

# 超时
# 思路1、没有负权回路理论上n-1次松弛后路径就不变了，有负权回路n次路径更新还会改变。判断n次minDist是否改变
# 时间复杂度 n*e

# # 将所有边和权值保存即可
# edges = []
# for _ in range(m):
#     edges.append(list(map(int, input().split())))
# # print(edges)
# 做n次松弛  # 多1次松弛为了看是否有负权回路
# update = False  # 判断是否还需要更新
# for i in range(n):
#     update = False
#     for s, t, v in edges:
#         if minDist[s] != max_int and minDist[s] + v < minDist[t]:
#             if i < n-1:
#                 minDist[t] = minDist[s] + v
#             update = True
#
#     if not update:
#         break
# if update:
#     print("circle")
# elif minDist[end] != max_int:
#     print(minDist[end])
# else:
#     print("unconnected")

# 已AC
# 思路2、使用SPFA算法，无负权回路下每个节点最多进入队列n-1次，超出则表示有负权回路
grid = [[] for _ in range(n+1)]
for _ in range(m):
    s, t, v = map(int, input().split())
    grid[s].append([t,v])

count = [0] * (n+1)  # 记录节点加入队列次数，用以判断是否有负权回路

que = deque()
que.append(start)
count[start] += 1
flag = False
while que:
    cur_s = que.popleft()
    for cur_t, cur_v in grid[cur_s]:
        if minDist[cur_s] + cur_v < minDist[cur_t]:
            minDist[cur_t] = minDist[cur_s] + cur_v
            count[cur_t] += 1
            if count[cur_t] == n:
                flag = True
                que.clear()
                break
            que.append(cur_t)

if flag:
    print("circle")
elif minDist[end] != max_int:
    print(minDist[end])
else:
    print("unconnected")
