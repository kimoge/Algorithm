# 题目：mXn的矩阵，从（0,0）->（m-1，n-1）有多少种不同的做法

# 1、dp[i][j]：到矩阵(i,j)的做法
# 2、dp[i][j] = dp[i-1][j] + dp[i][j-1]
# 3、dp初始化：初始化边界值
# 4、遍历顺序：先行后列，从前到后
# 5、打印dp数组
m = 4
n = 6

# 直接全部初始化为1
dp = [[1] * n for _ in range(m)]

# 从（1,1）开始向左右更新即可
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

for i in dp:
    for j in i:
        print(j, end=" ")
    print()