# 并查集模版
n = 1000  # 比节点数大就好，根据要求自行设置
father = [0] * n
rank = [1] * n  # 不使用路径压缩方法，使用按秩合并方法


def init():
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

    # # 按秩合并策略
    # if rank[u] <= rank[v]:
    #     father[u] = v
    # else:
    #     father[v] = u
    #
    # if rank[u] == rank[v] and u != v:
    #     rank[v] += 1


