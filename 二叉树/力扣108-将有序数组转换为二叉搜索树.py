class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        curNodeIndex = len(nums)//2
        curNode = TreeNode(nums[curNodeIndex])

        curNode.left = self.sortedArrayToBST(nums[:curNodeIndex])
        curNode.right = self.sortedArrayToBST(nums[curNodeIndex+1:])

        return curNode