def postorder_recur(root):
    """
    后序遍历+最大高度
    最大高度==最大深度
    结果作为返回值返回
    """
    if not root:
        return 0
    return max(postorder_recur(root.left), postorder_recur(root.right)) + 1


max_deep = [0]  # 为了使之后的操作结果返回，需要保持地址不变
def inorder_recur_1(root, deep, max_deep):
    """
    前序遍历+最大深度
    因为需要先判断当前层高度再判断左右子树
    结果保存在max_deep这个外部数据中
    """
    if not root:
        return
    max_deep[0] = max(max_deep[0], deep)
    inorder_recur_1(root.left, deep + 1, max_deep)
    inorder_recur_1(root.right, deep + 1, max_deep)


def inorder_recur_2(root, deep, max_deep):
    """
    前序遍历+最大深度
    因为需要先判断当前层高度再判断左右子树
    结果返回
    """
    if not root:
        return max_deep
    max_deep = max(max_deep, deep)
    return max(inorder_recur_2(root.left, deep + 1, max_deep),
                inorder_recur_2(root.right, deep + 1, max_deep))





