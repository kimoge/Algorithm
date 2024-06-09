class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        递归法
        """
        if not root or root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)

    def searchBST_1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        迭代法
        """
        while root:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            elif root.val == val:
                return root

        return None


