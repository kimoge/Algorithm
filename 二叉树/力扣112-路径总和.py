class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            return self.recur(root, 0, targetSum)
        return False

    def recur(self, root, sum, targetSum):
        sum += root.val
        # 终止条件：叶节点+判断
        if not root.left and not root.right:
            if sum == targetSum:
                return True
            return False

        if root.left and self.recur(root.left, sum, targetSum):
            return True
        if root.right and self.recur(root.right, sum, targetSum):
            return True

        return False
