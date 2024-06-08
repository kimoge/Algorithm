class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.recur(inorder, postorder)

    def recur(self, inorder, postorder):
        if not postorder or not inorder:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        root.right = self.recur(inorder[root_index+1:], postorder)
        root.left = self.recur(inorder[:root_index], postorder)

        return root
