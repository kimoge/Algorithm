# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root):
        self.res = 0
        if self.postOrder(root) == 0:
            self.res += 1
        return self.res

    def postOrder(self, root):
        """
        0：无覆盖
        1：有覆盖
        2：有摄像头
        """
        if not root:
            return 1

        left = self.postOrder(root.left)
        right = self.postOrder(root.right)

        if left == 1 and right == 1:
            return 0
        elif left == 0 or right == 0:
            self.res += 1
            return 2
        elif left == 2 or right == 2:
            return 1
