# 0-1背包


# 1、dp[i][j] :i个0、j个1有dp[i][j]个元素构成
# 2、递推公式：dp[i][j] = max(dp[i][j], dp[i-x][j-y] + 1)
# x:当前所选元素中0的个数，y：当前所选元素中1的个数
# 3、初始化：dp[0][0] = 0, dp全部初始为0
# 4、遍历顺序：先物品，再背包，背包逆序遍历
# 5、打印dp数组

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3

dp = [[0] * (n + 1) for _ in range(m + 1)]

for str in strs:
    x = 0
    y = 0
    for i in str:
        if i == "0":
            x += 1
        elif i == "1":
            y += 1
    for i in range(m, x-1, -1):
        for j in range(n, y-1, -1):
            # if i >= x and j >= y:
            dp[i][j] = max(dp[i][j], dp[i-x][j-y] + 1)

print(dp[-1][-1])
# for i in dp:
#     for j in i:
#         print(j, end=" ")
#     print()