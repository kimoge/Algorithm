class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        前中后序均可
        """
        # 因为必有结果，不会执行到最底层，所以该代码其实不必写
        if not root:
            return None

        # 当前值比p、q都大，向左寻找
        if root.val > q.val and root.val > p.val:
            left = self.lowestCommonAncestor(root.left, p, q)
            if left:
                return left
        # 当前值比p、q都小，向右寻找
        elif p.val > root.val and q.val > root.val:
            right = self.lowestCommonAncestor(root.right, p, q)
            if right:
                return right

        return root