# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def postorder_recur(root):
    """
    递归法+后序遍历
    """
    if not root:
        return root
    l = postorder_recur(root.left)
    r = postorder_recur(root.right)
    root.left, root.right = r, l
    return root


def inorder_recur(root):
    """
    递归法+前序遍历
    """
    if not root:
        return root
    # 交换左右子树
    root.left, root.right = root.right, root.left
    # 翻转左右子树
    inorder_recur(root.left)
    inorder_recur(root.right)

    return root






