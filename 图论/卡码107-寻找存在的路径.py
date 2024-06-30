father = [0] * (100 + 1)


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


n, m = map(int, input().split())
init(n+1)

for _ in range(m):
    s, t = map(int, input().split())
    join(s, t)

source, destination = map(int, input().split())

if isSame(source, destination):
    print(1)
else:
    print(0)



