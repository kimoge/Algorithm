nums = [0,0,0]
nums.sort()

res = []
for i in range(len(nums)-2):
    # 去重
    if i > 0 and nums[i] == nums[i-1]:
        continue
    l = i + 1
    r = len(nums) - 1
    while l < r:
        if nums[i] + nums[l] + nums[r] == 0:
            res.append([nums[i], nums[l], nums[r]])
            l += 1
            r -= 1
            # 去重
            while l < r and nums[l] == nums[l-1]:
                l += 1
            while l < r and nums[r] == nums[r+1]:
                r -= 1

        elif nums[i] + nums[l] + nums[r] > 0:
            r -= 1
        elif nums[i] + nums[l] + nums[r] < 0:
            l += 1

print(res)
