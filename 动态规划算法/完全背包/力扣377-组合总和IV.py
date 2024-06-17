# 完全背包

# dp[j]: 容量为j背包排列有dp[j]种
# dp[j] += dp[j-nums[i]]
# dp[0] = 1
# 排列问题，先背包后物品

nums = [1,2,3]
target = 4

dp = [0] * (target + 1)
dp[0] = 1

for j in range(len(dp)):
    for i in range(len(nums)):
        if j >= nums[i]:
            dp[j] += dp[j - nums[i]]

print(dp)