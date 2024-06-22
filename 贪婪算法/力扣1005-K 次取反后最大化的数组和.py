nums = [2,-3,-1,5,-4]
k = 2

# 根据绝对值从小到大排序
nums.sort(key=lambda x:abs(x))

# 先更新绝对值大的负数
for i in range(len(nums)-1, -1, -1):
    if nums[i] < 0 and k > 0:
        nums[i] *= -1
        k -= 1

# k大于0且为奇数，则将绝对值最小的正数修改
if k % 2 == 1:
    nums[0] *= -1
print(sum(nums))
