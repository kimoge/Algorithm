nums = [2,3,1,1,4]

scope = 0
i = 0
while i <= scope:
    # 更新scope范围
    scope = max(scope, nums[i] + i)
    # 如果覆盖最后值，即可以跳到
    if scope >= len(nums) - 1:
        break
    i += 1

print(scope)
