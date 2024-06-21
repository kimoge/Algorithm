nums = [1, 2, 1]
# 单调栈
res = [-1] * len(nums)
stack = [0]  # 存放遍历过的元素

# 遍历两遍
for i in range(1, len(nums) * 2):
    # 没有找到比遍历过得栈首元素大的
    if nums[stack[-1]] >= nums[i % len(nums)]:
        stack.append(i % len(nums))
    else:
        # 找到比栈首元素大的
        while stack and nums[stack[-1]] < nums[i % len(nums)]:
            temp = stack.pop()
            res[temp] = nums[i % len(nums)]
        stack.append(i % len(nums))
print(res)