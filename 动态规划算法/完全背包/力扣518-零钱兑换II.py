# 完全背包
# 组合问题：先物品后背包
# 排列问题：先背包后物品

# 1、dp[j]:j容量背包有dp[j]种装法
# 2、递推公式：dp[j] += dp[j - coins[i]]
# 3、遍历顺序：顺序，由于是组合方案，所以先物品后背包
# 4、初始化：dp[0] = 1,其余为0
# 5、打印dp数组


amount = 5
coins = [1, 2, 5]


dp = [0] * (amount+1)
dp[0] = 1

for i in range(len(coins)):
    for j in range(coins[i], len(dp)):
        dp[j] += dp[j-coins[i]]

# print(dp)
print(dp[-1])