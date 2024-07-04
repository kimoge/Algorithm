# 求最短路径 + 路径权值出现负数时 使用Bellman-ford算法
# 时间复杂度 n*e
n, m = map(int, input().split())
max_int = 101
# 将所有边和权值保存即可
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
# print(edges)
start = 1  # 起点
end = n  # 终点

minDist = [max_int] * (n + 1)
minDist[start] = 0  # 初始化起点最短距离

# 做n-1次松弛
for _ in range(n - 1):
    update = False  # 判断本次是否有更新
    for s, t, v in edges:
        if minDist[s] != max_int and minDist[s] + v < minDist[t]:
            minDist[t] = minDist[s] + v
            update = True
    if not update:
        break

if minDist[end] != max_int:
    print(minDist[end])
else:
    print("unconnected")