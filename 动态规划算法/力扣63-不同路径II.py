# 1、dp[i][j]：到obstacleGrid(i, j)的方法个数
# 2、递推公式：if obstacleGrid[i][j]==1 dp[i][j] = 0;
#             else dp[i][j] = dp[i-1][j] + dp[i][j-1]
# 3、初始化：第一行、第一列按照obstacleGrid值初始化
# 4、遍历顺序：从上到下，从左到右
# 5、打印dp数组
obstacleGrid = [[0,0]]

m = len(obstacleGrid)
n = len(obstacleGrid[0])

dp = [[0] * n for _ in range(m)]

for i in range(m):
    if obstacleGrid[i][0] == 1:
        break
    dp[i][0] = 1

for i in range(n):
    if obstacleGrid[0][i] == 1:
        break
    dp[0][i] = 1

for i in range(1, m):
    for j in range(1, n):
        if obstacleGrid[i][j] == 1:
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[m-1][n-1])
