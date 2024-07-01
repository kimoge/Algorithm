# case1:有入度为2节点，且两边都可删
# case2:有入读为2节点，且只有一条边可删
# case3:没有入度为2节点但有环，去除环

import sys

father = [0] * (1000 + 1)


def init(n):
    """
    初始化并查集
    """
    for i in range(n):
        father[i] = i


def find(u):
    """
    找u的根
    """
    if u == father[u]:
        return u
    else:
        father[u] = find(father[u])  # 路径压缩
        return father[u]


def isSame(u, v):
    """
    判断是否根相同
    """
    u = find(u)
    v = find(v)
    if u == v:
        return True
    else:
        return False


def join(u, v):
    """
    u、v集合合并
    """
    u = find(u)
    v = find(v)

    # 路径压缩合并策略,将v所在集合并入u的集合里
    if v == u:
        return
    father[v] = u


def isTreeAfterRemoveEdge(edges, deleteEdge, n):
    """
    判断删除边后是否为有向树
    """
    init(n + 1)
    for i in range(len(edges)):
        if deleteEdge == edges[i]:
            continue
        if isSame(edges[i][0], edges[i][1]):
            return False
        join(edges[i][0], edges[i][1])

    return True


def getRemoveEdge(edges, n):
    """
    找到环中要删除的节点
    """
    init(n + 1)
    for i in range(len(edges)):
        if isSame(edges[i][0], edges[i][1]):
            print(edges[i][0], edges[i][1])
            return
        else:
            join(edges[i][0], edges[i][1])


n = int(input())

edges = []  # 记录边
inDegree = [0] * (n + 1)  # 入度初始化为0
for _ in range(n):
    s, t = map(int, input().split())
    inDegree[t] += 1
    edges.append([s, t])


may_res = []  # 记录可能删除边

# 倒序查找入度为2的边，其可能就是要删除的边
for i in range(n - 1, -1, -1):
    if inDegree[edges[i][1]] == 2:
        may_res.append(edges[i])

# case1&&case2
# 如果存在入读为2的边，may_res一定有两个边
if may_res:
    if isTreeAfterRemoveEdge(edges, may_res[0], n):
        print(may_res[0][0], may_res[0][1])
    else:
        print(may_res[1][0], may_res[1][1])
    sys.exit()
# case3
getRemoveEdge(edges, n)



