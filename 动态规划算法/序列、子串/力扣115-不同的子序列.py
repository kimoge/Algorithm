# 1、dp[i][j]:0~i-1的s中出现0~j-1的t的个数
# 2、if s[i-1]==t[j-1]:    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
# (tips:包括s[i-1]匹配到t[0:j]的个数 + 不包括s[i-1]匹配到t[0:j]的个数)
# else:   dp[i][j] = dp[i-1][j]
# (tips:s[i-1]匹配不了，只能赋值为不包括s[i-1]匹配到的个数)
# 3、初始化：dp数组第一列为1，第一行除第一个元素其他为0
# 4、左上 -> 右下

s = "rabbbit"
t = "rabbit"

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

for i in range(len(s) + 1):
    dp[i][0] = 1

for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i-1]==t[j-1]:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])