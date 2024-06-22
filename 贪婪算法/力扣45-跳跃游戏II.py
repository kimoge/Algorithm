nums = [2,3,1,1,4]

if len(nums) == 1:
     print(0)

# 当前可以跳的最大范围
cur_scope = 0
# 下一步数后可以跳的最大范围
next_scope = 0
i = 0
times = 0
while i <= cur_scope:
    # 更新
    next_scope = max(next_scope, nums[i] + i)

    # 超出本次能跳的范围，步数+1,更新当前范围
    if cur_scope == i:
        times += 1
        cur_scope = next_scope
        # 当前步数范围包含最后，结束循环
        if cur_scope >= len(nums) - 1:
            break

    i += 1

print(times)