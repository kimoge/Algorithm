class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # return self.buildTree(nums)
        return self.buildTreeOptimize(nums, 0, len(nums))

    def buildTree(self, nums):
        if not nums:
            return None

        max_num = max(nums)
        max_index = nums.index(max_num)
        curNode = TreeNode(max_num)

        curNode.left = self.buildTree(nums[:max_index])
        curNode.right = self.buildTree(nums[max_index+1:])

        return curNode

    def buildTreeOptimize(self, nums, start, end):
        """
        start-end：左闭右开
        """
        if start == end:
            return None

        max_num = -1
        max_index = -1
        for i in range(start, end):
            if nums[i] > max_num:
                max_num = nums[i]
                max_index = i

        curNode = TreeNode(max_num)
        curNode.left = self.buildTreeOptimize(nums, start, max_index)
        curNode.right = self.buildTreeOptimize(nums, max_index+1, end)

        return curNode