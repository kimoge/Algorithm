# 完全背包
import math

# 1、dp[j]：容量为j最少需要多少个正整数平方去凑
# 2、dp[j] = min(dp[j], dp[j -nums[i]] + 1)
# 3、初始化dp[0] = 0, 其他设最大n（n个1组成）
# 4、非组合、非排列问题，遍历顺序均可

n = 12

# 物品
nums_2 = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]

max_int = n
dp = [n] * (n+1)
dp[0] = 0

for i in range(len(nums_2)):
    for j in range(nums_2[i], len(dp)):
        dp[j] = min(dp[j], dp[j - nums_2[i]] + 1)

print(dp[n])


