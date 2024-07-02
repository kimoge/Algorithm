# 拓扑排序--有向图线性输出入度为0的结点---可以用来判断是否有环
from collections import deque

n, m = map(int, input().split())

inDegree = [0] * n  # 记录入度
grid = [[] for _ in range(n)]  # 邻接表
for _ in range(m):
    s, t = map(int, input().split())
    inDegree[t] += 1
    grid[s].append(t)

queue = deque()  # 使用队列保存入度为0的节点, 使用栈也是可以的
for i in range(n):
    if inDegree[i] == 0:
        queue.append(i)

res = []  # 保存拓扑排序结果
while queue:
    cur = queue.popleft()
    res.append(cur)

    # 将当前节点删除后更新inDegree表，并将入度为0的点加入队列或栈
    if grid[cur]:
        for j in grid[cur]:
            inDegree[j] -= 1
            if inDegree[j] == 0:
                queue.append(j)


if len(res) == n:
    for i in range(n-1):
        print(res[i], end=" ")
    print(res[n-1])
else:
    print(-1)