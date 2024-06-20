# 1、dp[i][j]:0~i-1的text1和0~j-1的text2最长公共子序列（可以不连续）
# 2、text1[i-1] == text2[j-1]  :    dp[i][j] = dp[i-1][j-1]
# else:   dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# 3、初始化均为0
# 4、遍历顺序：左上 -> 右下

text1 = "abcde"
text2 = "ace"

dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

for i in range(1, len(text1) + 1):
    for j in range(1, len(text2) + 1):
        if text1[i - 1] == text2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# print(dp)
print(dp[-1][-1])