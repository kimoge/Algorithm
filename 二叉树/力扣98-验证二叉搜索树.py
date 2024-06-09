import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.max_val = -sys.maxsize
        return self.inorder(root)

    def inorder(self, root):
        """
        中序遍历判断
        """
        if not root:
            return True

        left = self.inorder(root.left)

        if self.max_val > root.val:
            return False
        else:
            self.max_val = root.val

        right = self.inorder(root.right)

        return left and right




