# 1、dp[i][j]:word1[0~i-1]和word2[0~j-1]相同所需的最小步数
# 2、if word1[i-1] == word2[j-1] : dp[i][j] = dp[i-1][j-1]
# else:    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 2)
# (tips:删除word1[i-1]、删除word2[j-1]、两个都删除中取最小步数)
# 3、dp第一行赋值列的值，第一列赋值行的值
# 4、左上->右下

word1 = "sea"
word2 = "eat"

dp = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
for i in range(len(word1) + 1):
    dp[i][0] = i
for i in range(len(word2) + 1):
    dp[0][i] = i

for i in range(1, len(word1) + 1):
    for j in range(1, len(word2) + 1):
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 2)

print(dp)