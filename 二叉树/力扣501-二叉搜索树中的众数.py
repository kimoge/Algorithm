class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.maxCount = 0
        self.count = 0
        self.result = []
        self.pre = None
        self.searchBST(root)
        return self.result

    def searchBST(self, root):
        """
        中序遍历
        """
        if not root:
            return

        self.searchBST(root.left)

        if not self.pre or self.pre.val == root.val:
            self.count += 1
        else:
            self.count = 1
        self.pre = root

        if self.maxCount == self.count:
            self.result.append(root.val)
        elif self.maxCount < self.count:
            self.maxCount = self.count
            self.result = [root.val]

        self.searchBST(root.right)
