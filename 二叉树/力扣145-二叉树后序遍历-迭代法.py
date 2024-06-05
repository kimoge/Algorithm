from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

root = None

stack = []
res = deque()

if root:
    stack.append(root)

while stack:
    cur = stack.pop()
    if cur.left:
        stack.append(cur.left)
    if cur.right:
        stack.append(cur.right)
    res.appendleft(cur.val)

print(list(res))