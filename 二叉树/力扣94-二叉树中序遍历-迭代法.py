# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


root = None
cur = root
stack = []
res = []

while cur or stack:
    if cur:
        stack.append(cur)
        cur = cur.left
    else:
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right

print(res)