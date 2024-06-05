class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归实现
        res = []
        self.inorder_cur(root, res)
        return res

    def inorder_cur(self, root, res):
        """
        递归实现中序遍历
        """
        if not root:
            return
        self.inorder_cur(root.left, res)
        res.append(root.val)
        self.inorder_cur(root.right, res)