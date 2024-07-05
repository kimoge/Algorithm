import sys
n, m = map(int, input().split())
max_int = sys.maxsize
# 将所有边和权值保存即可
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
# print(edges)
start, end, k = map(int, input().split())

minDist = [max_int] * (n + 1)
minDist[start] = 0  # 初始化起点最短距离
# 做k+1次松弛
for _ in range(k+1):
    update = False  # 判断本次是否有更新
    minDist_copy = minDist.copy()
    for s, t, v in edges:
        if minDist[s] != max_int and minDist_copy[s] + v < minDist[t]:
            minDist[t] = minDist_copy[s] + v
            update = True
    if not update:
        break
# print(minDist)
if minDist[end] != max_int:
    print(minDist[end])
else:
    print("unreachable")