nums = [-1,0,-5,-2,-2,-4,0,1,-2]
target = -9

result = []
nums.sort()
print(nums)
for i in range(len(nums) - 3):
    # 剪枝
    if nums[i] > target and nums[i] > 0:
        break

    # 对nums[i]去重
    if i > 0 and nums[i] == nums[i - 1]:
        continue
        
    for j in range(i+1, len(nums) - 2):
        # 剪枝
        if nums[i] + nums[j] > target and nums[j] > 0:
            break

        # 对nums[j]去重
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue
            
        left = j + 1
        right = len(nums) - 1
        while left < right:
            sum_num = nums[i] + nums[j] + nums[left] + nums[right]
            if sum_num == target:
                result.append([nums[i], nums[j], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif sum_num > target:
                right -= 1
            elif sum_num < target:
                left += 1
        
print(result)