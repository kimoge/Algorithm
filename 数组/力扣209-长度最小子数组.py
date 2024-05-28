# 双指针
target = 7
nums = [2,3,1,2,4,3]

# 左闭右闭区间
l = 0
r = 0
res = 0
min_length = len(nums)
sum_nums = 0
while l <= r < len(nums):
    res += nums[r]
    sum_nums += nums[r]
    while res >= target:
        min_length = min(r - l + 1, min_length)
        res -= nums[l]
        l += 1
    r += 1
print(sum_nums)
print(min_length)