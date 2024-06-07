class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) == -1:
            return False
        return True

    def getHeight(self, root):
        """
        后序遍历判断二叉树是否平衡
        return：-1:不平衡；其他：平衡
        """
        if not root:
            return 0

        lHeight = self.getHeight(root.left)
        rHeight = self.getHeight(root.right)

        if lHeight == -1 or rHeight == -1:
            return -1
        elif abs(lHeight - rHeight) > 1:
            return -1

        return max(lHeight, rHeight) + 1
