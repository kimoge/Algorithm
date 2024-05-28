# 双指针
target = 7
nums = [2, 3, 1, 2, 4, 3]

# 左闭右闭区间
left = 0
right = 0
res = 0
min_length = len(nums)
# while left <= right < len(nums):
while right < len(nums):
    res += nums[right]
    while res >= target:
        min_length = min(right - left + 1, min_length)
        res -= nums[left]
        left += 1
    right += 1

print(min_length)
