# 1、dp[i][j]:第i+1天状态为j时股票所得最大利润
#     0：不操作
#     1：持有
#     2：不持有
# 2、dp[i][0] = 0
#     dp[i][1] = max(dp[i-1][1], dp[i-1][2] - prices[i])
#     dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i] - fee)
# 3、初始化：dp[0][0] = 0, dp[0][1] = -prices[0], dp[0][2] = 0
# 4、遍历顺序：左到右
# 5、打印dp数组

prices = [1, 3, 2, 8, 4, 9]
fee = 2

dp = [[0] * 3 for i in range(len(prices))]

dp[0][0] = 0
dp[0][1] = -prices[0]
dp[0][2] = 0

for i in range(1, len(prices)):
    dp[i][1] = max(dp[i-1][1], dp[i-1][2] - prices[i])
    dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i] - fee)


print(dp[-1][2])
