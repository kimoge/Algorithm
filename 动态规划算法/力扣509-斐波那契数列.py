# 0 1 1 2 3 5 8 。。。
# 1、dp数组、下标含义:dp[i]第i个斐波那契数
# 2、递推公式：dp[i] = dp[i-1] + dp[i-2]
# 3、di数组初始化:dp[0] = dp[1] = 1
# 4、遍历顺序：从前到后
# 5、打印dp数组
n = int(input())
dp = [0] * (n + 1)
if n == 0:
    print(0)
if n == 1:
    print(1)

dp[0] = 0
dp[1] = 1
if n>=2:
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]



for i in dp:
    print(i, end=" ")
