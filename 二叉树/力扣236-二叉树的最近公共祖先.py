class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        后序遍历查找最近公共祖先
        """
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 左不空右空
        if left and not right:
            return left
        # 左空右不空
        elif not left and right:
            return right
        # 左右都不空
        elif left and right:
            return root
        # 左右都为空
        return None