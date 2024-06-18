class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root):
        return max(self.dp(root))

    def dp(self, root):
        if not root:
            return [0, 0]  # 0位：不偷root；1位：偷root

        left = self.dp(root.left)
        right = self.dp(root.root)

        # 不偷root
        val0 = max(left[0], left[1]) + max(right[0], right[1])
        # 偷root
        val1 = root.val + left[0] + right[0]

        return [val0, val1]