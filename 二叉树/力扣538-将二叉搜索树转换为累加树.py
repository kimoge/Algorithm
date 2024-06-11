class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = None
        self.reinorder(root)
        return root

    def reinorder(self, root):
        """
        右中左顺序遍历
        """
        if not root:
            return

        self.reinorder(root.right)

        if self.pre:
            root.val += self.pre.val
        self.pre = root

        self.reinorder(root.left)