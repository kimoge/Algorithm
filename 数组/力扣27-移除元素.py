# 双指针（快慢指针）删除元素
nums = [0, 1, 2, 2, 3 , 0, 4, 2]
val = 2

fast = 0
low = 0
while fast < len(nums):
    nums[low] = nums[fast]
    # 当low指针值等于val时，需要停在原地根据fast指针赋值；否则移动
    if nums[low] != val:
        low += 1

    # fast指针每次正常移动
    fast += 1

print(nums, low)

