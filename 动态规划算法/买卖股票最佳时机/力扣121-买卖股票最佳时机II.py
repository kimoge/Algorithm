# 1、dp[i][0]:第i+1天不持有股票所得最大利润
# dp[i][1]：第i+1天持有股票所得最大利润
# 2、dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
# 3、初始化：dp[0][0] = 0
# dp[0][1] = - price[0]
# 4、遍历顺序：左到右
# 5、打印dp数组

prices = [7,1,5,3,6,4]

dp = [[0,0] for i in range(len(prices))]

dp[0][0] = 0
dp[0][1] = - prices[0]

for i in range(1, len(prices)):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
    dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

print(dp[-1][0])