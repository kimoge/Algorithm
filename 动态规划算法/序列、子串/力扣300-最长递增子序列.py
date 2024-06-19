# 1、dp[i]:确定将i加入子序列时严格递增子序列最长长度
# 2、if nums[i] > nums[i-1]: dp[i] = max(dp[i], dp[j] + 1)
# else dp[i-1]
# 3、dp[0] = 1
# 4、从左到右
# 5、打印dp数组

nums = [1,3,6,7,9,4,10,5,6]

dp = [1] * len(nums)

for i in range(1, len(dp)):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)