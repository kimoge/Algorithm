def postorder_recur(left, right):
    """
    两树+递归法+后序遍历
    """
    # 左右都为空节点
    if not left and not right:
        return True
    # 左空右不空
    elif not left and right:
        return False
    # 左不空右空
    elif left and not right:
        return False
    # 左右都不空，但值不同，此处可以看做是一个剪枝操作，正常是放在递归逻辑处判断
    elif left.val != right.val:
        return False

    outside = postorder_recur(left.left, right.right)
    inside = postorder_recur(left.right, right.left)
    return outside and inside
