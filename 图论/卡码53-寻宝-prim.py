# 最小生成树之prim（加节点）
# 步骤：1、寻找距离生成树最短距离节点；2、将节点加入生成树；3、更新minDist表

v, e = map(int, input().split())
# 邻接矩阵
grid = [[10001] * (v + 1) for _ in range(v + 1)]
for i in range(e):
    v1, v2, val = map(int, input().split())
    grid[v1][v2] = val
    grid[v2][v1] = val

# minDist
minDist = [10001] * (v + 1)
isInTree = [False] * (v + 1)

# 依次加入所有节点
for i in range(1, v+1):
    # 1、选取当前最小距离结点加入生成树
    cur = -1
    minVal = 10002
    for j in range(1, v + 1):
        if not isInTree[j] and minVal > minDist[j]:
            cur = j
            minVal = minDist[j]
    # 2、加入生成树
    isInTree[cur] = True

    # 3、更新minDist数组
    for j in range(1, v + 1):
        if not isInTree[j] and grid[cur][j] < minDist[j]:
            minDist[j] = grid[cur][j]

# print(isInTree)
# print(minDist)
res = 0
for i in range(2, v + 1):
    res += minDist[i]

print(res)


