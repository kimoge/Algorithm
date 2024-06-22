nums = [-2,1,-3,4,-1,2,1,-5,4]

res = min(nums)
cur_sum = 0
for i in range(len(nums)):
    cur_sum += nums[i]
    res = max(cur_sum, res)
    if cur_sum < 0:
        cur_sum = 0

print(res)