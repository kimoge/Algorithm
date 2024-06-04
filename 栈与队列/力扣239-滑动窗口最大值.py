from collections import deque


# 双端队列去做单调队列实现
class Solution:
    def __init__(self):
        self.queue = deque()

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        for i in range(k):
            self.push(nums[i])
        l, r = 0, k  # 左闭右开
        res.append(self.getMax())
        while r < len(nums):
            self.pop(nums[l])
            self.push(nums[r])
            res.append(self.getMax())
            l += 1
            r += 1
        return res

    def push(self, x):
        # 当push元素时，去除队首和队尾比x小的元素，再把x加在队尾
        while self.queue and self.queue[-1] < x:
            self.queue.pop()
        while self.queue and self.queue[0] < x:
            self.queue.popleft()
        self.queue.append(x)

    def pop(self, x):
        # 当队首元素是要删除的元素才真正的pop
        if self.queue[0] == x:
            self.queue.popleft()

    def getMax(self):
        # 队首元素就是当前队内最大值
        return self.queue[0]


nums = [1,3,1,2,0,5]
k = 3
s = Solution()
print(s.maxSlidingWindow(nums, k))
