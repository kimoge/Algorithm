class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.preorder(root1, root2)

    def preorder(self, root1, root2):
        """
        前序遍历合并二叉树
        """
        if not root1 and not root2:
            return None
        elif not root1 and root2:
            return root2
        elif root1 and not root2:
            return root1

        curNode = TreeNode(root1.val + root2.val)
        curNode.left = self.preorder(root1.left, root2.left)
        curNode.right = self.preorder(root1.right, root2.right)

        return curNode