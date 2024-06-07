# 注意：最小深度是根节点到叶子结点的最小深度or最小高度
def getMinDepth(root):
    """
    后序求最小高度==最小深度
    """
    if not root:
        return 0

    # 左不空右空
    if root.left and not root.right:
        return 1 + getMinDepth(root.left)
    # 左空右不空
    elif not root.left and root.right:
        return 1 + getMinDepth(root.right)
    else:
        return 1 + min(getMinDepth(root.left), getMinDepth(root.right))
