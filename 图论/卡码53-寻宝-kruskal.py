# 最小生成树之kruskal 时间复杂度：eloge(边排序)+e(遍历)

# 遍历边
# 1、找最小的一条边
# 2、判断是否在生成树中
# 3、不在，加入边；在，不加入。返回步骤1继续

father = [0] * 10001


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

    # # 按秩合并策略
    # if rank[u] <= rank[v]:
    #     father[u] = v
    # else:
    #     father[v] = u
    #
    # if rank[u] == rank[v] and u != v:
    #     rank[v] += 1


v, e = map(int, input().split())

edges = []
for _ in range(e):
    edges.append(list(map(int, input().split())))

# 按权重递增排序
edges.sort(key=lambda x:x[2])
# print(edges)

init(v+1)
res = 0
res_edges = []
for v1, v2, val in edges:
    if isSame(v1, v2):
        continue
    else:
        res += val
        res_edges.append([v1, v2, val])
        join(v1, v2)

print(res)
print(res_edges)