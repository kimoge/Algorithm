# 1、dp[i][j]:s[i~j](左闭右闭)之间的最长回文子序列长度
# 2、if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
#   else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
# 3、初始化：dp对角线元素赋值为1
# 4、遍历顺序：左下->右上

s = "cbbd"

dp = [[0] * len(s) for _ in range(len(s))]

for i in range(len(dp)):
    dp[i][i] = 1

for i in range(len(s) - 2, -1, -1):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            dp[i][j] = dp[i + 1][j - 1] + 2
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])

for i in dp:
    print(i)
print(dp[0][len(s) - 1])