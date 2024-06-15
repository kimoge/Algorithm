# 1、dp[j]：当前个物品中背包容量为j的最大价值
# 2、递推公式dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
# 3、初始化：根据是否放入物品0的情况
# 4、遍历顺序：从左到右
# 5、打印dp数组

weight = [1, 3, 4]
value = [15, 20, 30]

dp = [0] * (max(weight) + 1)

for i in range(len(dp)):
    if i >= weight[0]:
        dp[i] = value[0]

# 更新3-1=2次
for i in range(1, len(weight)):
    # 倒序遍历才是0-1背包，否则是完全背包，即一个物品可能重复使用
    for j in range(len(dp)-1, weight[i] - 1, -1):
        # if j >= weight[i]:
        dp[j] = max(dp[j-weight[i]] + value[i], dp[j])

for i in dp:
    print(i, end=" ")