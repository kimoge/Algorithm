# 1、dp数组及下标含义：dp[i]:爬i阶楼梯的方法数
# 2、递推公式：dp[i] = dp[i-1] + dp[i-2] notes:一次爬1阶或2阶楼梯，看题目情况
# 3、dp数组初始化 dp[0] = 1, dp[1] = 1
# 4、遍历顺序：从前到后
# 5、打印dp数组，debug发现错误

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
if n>=2:
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

for i in dp:
    print(i, end=" ")