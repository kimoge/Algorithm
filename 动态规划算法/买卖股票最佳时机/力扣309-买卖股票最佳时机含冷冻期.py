# 1、dp[i][j]:第i+1天状态为j时股票所得最大利润
#     0：不操作
#     1：持有
#     2：当天卖出不持有
#     3：昨天卖出不持有，即冷冻期
#     4：昨天以前卖出不持有，即超出冷冻期
# 2、dp[i][0] = 0
#     dp[i][1] = max(dp[i-1][1], dp[i-1][3] - prices[i], dp[i-1][4] - prices[i])
#     dp[i][2] = dp[i-1][1] + prices[i]
#     dp[i][3] = dp[i-1][2]
#     dp[i][4] = max(dp[i-1][3], dp[i-1][4])
# 3、初始化：dp[0][0] = 0, dp[0][1] = -prices[0], dp[0][2] = 0
# dp[0][3] = 0, dp[0][4] = 0
# 4、遍历顺序：左到右
# 5、打印dp数组

#
prices = [1,2,3,0,2]

dp = [[0] * 5 for i in range(len(prices))]

dp[0][0] = 0
dp[0][1] = -prices[0]
dp[0][2] = 0
dp[0][3] = 0
dp[0][4] = 0

for i in range(1, len(prices)):
    dp[i][1] = max(dp[i - 1][1], dp[i - 1][3] - prices[i], dp[i - 1][4] - prices[i])
    dp[i][2] = dp[i - 1][1] + prices[i]
    dp[i][3] = dp[i - 1][2]
    dp[i][4] = max(dp[i - 1][3], dp[i - 1][4])

print(max(dp[-1]))
