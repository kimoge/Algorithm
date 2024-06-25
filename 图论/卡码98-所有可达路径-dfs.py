def dfs(graph, x, res, path):
    if x == n:
        res.append(path.copy())
        return

    for i in range(1, n+1):
        if graph[x][i] == 1:
            path.append(i)
            dfs(graph, i, res, path)
            path.pop()


n, m = map(int, input().split())

# method1：使用邻接矩阵
graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    s, t = map(int, input().split())
    graph[s][t] = 1

res = []
dfs(graph, 1, res, [1])
# print(res)

for i in res:
    print(" ".join(list(map(str, i))))