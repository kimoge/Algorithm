# 1、dp数组、下标含义 dp[i]:到第i+1阶楼梯需要花费的体力
# 2、递推公式 dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
# 3、dp初始化 dp[0] = 0, dp[1] = 0, 题目规定，不必纠结
# 4、遍历顺序：从前往后
# 5、dp数组打印

cost = [10, 15, 20]
dp = [0] * (len(cost)+1) # 楼顶比cost多1
dp[0] = 0
dp[1] = 0

for i in range(2, len(dp)):
    dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

for i in dp:
    print(i, end=" ")