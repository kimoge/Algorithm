import sys
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.pre = None
        self.min_abs = sys.maxsize
        self.inorder(root)
        return self.min_abs

    def inorder(self, root):
        """
        中序遍历二叉搜索树
        """
        if not root:
            return

        self.inorder(root.left)

        if self.pre:
            self.min_abs = min(self.min_abs, root.val - self.pre.val)
        self.pre = root

        self.inorder(root.right)