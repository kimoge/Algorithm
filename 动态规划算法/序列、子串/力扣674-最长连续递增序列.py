# 1、dp[i]:确定将i加入子序列时严格连续递增子序列最长长度
# 2、if nums[i] > nums[i-1]: dp[i] = max(dp[i], dp[i-1] + 1)
# else 1
# 3、dp[0] = 1
# 4、从左到右
# 5、打印dp数组

nums = [1,3,5,4,7]

dp = [1] * len(nums)

for i in range(1, len(dp)):
    if nums[i] > nums[i-1]:
        dp[i] = dp[i-1] + 1

print(dp)