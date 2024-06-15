# 1、dp[i]：数i拆分后相乘所得的最大值
# 2、递推公式：for循环dp[i] = max(dp[i], j*(i-j), j * dp[i - j])
# 3、dp数组初始化
# 4、遍历顺序
# 5、打印dp数组
n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 0
dp[2] = 1
for i in range(3, n+1):
    for j in range(1, i//2 + 1):
        dp[i] =max(dp[i], j * (i - j), j * dp[i - j])  # dp[i]用于自我更新，j*(i-j)和j*dp[i-j]包含了所有拆分情况,因为dp[i-j]是必拆的,所以要加上不拆的情况

for i in dp:
    print(i, end=" ")

