from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return self.levelorder(root)

    def levelorder(self, root):
        """
        层序遍历
        """
        queue = deque()
        queue.append(root)
        res = None
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if i == 0:
                    res = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
