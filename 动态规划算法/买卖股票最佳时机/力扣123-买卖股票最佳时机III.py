# 1、dp[i][j]:第i+1天状态为j时股票所得最大利润
# 0：不操作
# 1：第一次持有
# 2：第一次不持有
# 3：第二次持有
# 4：第二次不持有
# 2、dp[i][0] = 0
# dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
# dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
# dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
# dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
# 3、初始化：dp[0][0] = 0, dp[0][1] = -prices[0], dp[0][2] = 0
# dp[0][3] = -prices[i], dp[0][4] = 0
# 4、遍历顺序：左到右
# 5、打印dp数组

prices = [7,1,5,3,6,4]

dp = [[0,0,0,0,0] for i in range(len(prices))]

dp[0][0] = 0
dp[0][1] = -prices[0]
dp[0][2] = 0
dp[0][3] = -prices[0]
dp[0][4] = 0

for i in range(1, len(prices)):
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
    dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
    dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])

print(dp[-1][4])