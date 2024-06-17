# 完全背包
import sys
# 1、dp[j]：容量为j的最少钱币组合有dp[j]个钱币
# 2、dp[j] = min(dp[j], dp[j-coins[i]] + 1)
# 3、dp[0] = 0,其余全为最大
# 4、组合问题，先物品后背包

coins = [1, 2, 5]
amount = 11

max_num = sys.maxsize
dp = [max_num] * (amount + 1)
dp[0] = 0

for i in range(len(coins)):
    for j in range(coins[i], len(dp)):
        dp[j] = min(dp[j], dp[j - coins[i]] + 1)

if dp[amount] != max_num:
    print(dp[amount])
else:
    print(-1)
# print(dp)
# print(dp[amount])