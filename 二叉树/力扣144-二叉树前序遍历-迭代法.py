# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 设计一个栈：
# 有元素时，pop栈顶元素，并push其右子树、左子树（为了最终实现中左右）
# 无元素时结束

stack = []  # 栈工具
res = []  # 存结果的集合

# 根节点先入栈
if root:
    stack.append(root)
while stack:
    cur = stack.pop()
    # 右不为空
    if cur.right:
        stack.append(cur.right)
    # 左不为空
    if cur.left:
        stack.append(cur.left)
    res.append(cur)

print(res)


