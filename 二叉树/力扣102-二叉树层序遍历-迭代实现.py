# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 队列实现
from collections import deque

root = None
queue = deque()
result = []
if root:
    queue.append(root)
while queue:
    # 获取当前层的元素
    res = []
    size = len(queue)
    for i in range(size):
        cur = queue.popleft()
        res.append(cur.val)

        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    result.append(res)

print(result)