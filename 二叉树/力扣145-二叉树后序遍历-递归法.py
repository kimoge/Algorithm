class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归实现
        res = []
        self.postorder_cur(root, res)
        return res

    def postorder_cur(self, root, res):
        """
        递归实现后序遍历
        """
        if not root:
            return
        self.postorder_cur(root.left, res)
        self.postorder_cur(root.right, res)
        res.append(root.val)