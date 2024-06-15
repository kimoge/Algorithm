# 0-1背包 不同种类物品各1个
# 完全背包  不同种类物品无限个
# 多成背包  不同种类物品不同多个


# 0-1背包问题
# 1、dp[i][j]:物品0-i之间取重量接近j的最大价值
# 2、递推公式：dp[i][j] = max(dp[i-1][j-weight[i]] + value[i], dp[i-1][j])
# 理解：0-i物品之间取i后重量是j的最大价值和不取i后重量是j的最大价值做比较取最大
# 3、初始化dp数组：dp[i][0] = 0 ;dp[0][j]按照真实情况初始化
# 4、遍历顺序：从左到右，从上到下
# 5、打印dp数组

weight = [1, 3, 4]
value = [15, 20, 30]

dp = [[0] * (max(weight) + 1) for _ in range(len(weight))]
for i in range(len(weight)):
    dp[i][0] = 0
for i in range(1, max(weight)+1):
    if i >= weight[0]:
        dp[0][i] = value[0]

for i in range(1, len(weight)):
    for j in range(1, max(weight)+1):
        # 判断数组下标是否越界
        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j-weight[i]] + value[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

for i in dp:
    for j in i:
        print(j, end=" ")
    print()
