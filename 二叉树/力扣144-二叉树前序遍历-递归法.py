class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: object[TreeNode]) -> list[int]:
        # 递归实现
        res = []
        self.preorder_cur(root, res)
        return res

    def preorder_cur(self, root, res):
        """
        递归实现前序遍历
        """
        if not root:
            return
        res.append(root.val)
        self.preorder_cur(root.left, res)
        self.preorder_cur(root.right, res)
