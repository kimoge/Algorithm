class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.postorder_recur(root)

    def postorder_recur(self, root):
        """
        递归+后序遍历查找左叶子结点
        获取当前节点的左叶子节点值之和
        """
        # 空节点
        if not root:
            return 0
        # 叶子结点
        if not root.left and not root.right:
            return 0

        left_val = self.postorder_recur(root.left)
        # 左叶子结点：该节点不空且左子树是叶子节点
        if root.left and not root.left.left and not root.left.right:
            left_val =  root.left.val
        right_val = self.postorder_recur(root.right)

        return left_val + right_val