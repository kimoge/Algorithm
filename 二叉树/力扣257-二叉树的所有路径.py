class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.getPath(root, [], res)
        return res

    def getPath(self, root, path, res):
        """
        获取所有路径
        """
        # 直接加入当前节点值
        path.append(root.val)

        # 当前节点为叶子结点时：收集路径
        if not root.left and not root.right:
            path = list(map(str, path))
            res.append("->".join(path))
            return

        # 左子树不为空，则递归左子树
        if root.left:
            self.getPath(root.left, path.copy(), res)
        # 右子树不为空，则递归右子树
        if root.right:
            self.getPath(root.right, path.copy(), res)


