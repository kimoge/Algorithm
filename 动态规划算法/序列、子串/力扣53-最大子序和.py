# 1、dp[i]:包括nums[i]的最大子序和
# 2、dp[i] = max(dp[i-1] + nums[i], nums[i])
# 3、dp[0] = nums[0]
# 4、左->右

nums = [-2,1,-3,4,-1,2,1,-5,4]

dp = [0] * len(nums)

dp[0] = nums[0]

for i in range(1, len(dp)):
    dp[i] = max(dp[i - 1] + nums[i], nums[i])

print(dp)