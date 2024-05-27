# 双指针方法
nums = [-4,-1,0,3,10]

result = [0] * len(nums)
l = 0
r = len(nums) - 1
index = len(nums) - 1

while l <= r:
    l_2 = nums[l]**2
    r_2 = nums[r]**2
    if l_2 < r_2:
        result[index] = r_2
        r -= 1
    else:
        result[index] = l_2
        l += 1

    index -= 1

print(result)
