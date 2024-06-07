class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # return self.getNodes(root)
        return self.getNodes_optimize(root)

    def getNodes(self, root):
        """
        常规解法：后序遍历
        """
        if not root:
            return 0
        return self.getNodes(root.left) + self.getNodes(root.right) + 1

    def getNodes_optimize(self, root):
        """
        根据完全二叉树的性质
        """
        # 终止条件增加：如果该节点为父节点的树是满二叉树：则利用满二叉树公式计算
        if not root:
            return 0

        left = root.left
        right = root.right
        left_depth, right_depth = 1, 1  # 左右子树初始高度为1（父节点高度为1）
        while left:
            left_depth += 1
            left = left.left
        while right:
            right_depth += 1
            right = right.right
        if right_depth == left_depth:
            return 2**right_depth - 1

        return self.getNodes(root.left) + self.getNodes(root.right) + 1


