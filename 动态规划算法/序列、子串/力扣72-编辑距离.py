# 与两个字符串删除操作求最小相似步数类似，区别在于递推公式的不等处赋值操作

word1 = "horse"
word2 = "ros"

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
            # 删除word1[i-1]、删除word2[j-1]、替换word1[i-1]或word2[j-1] 中取最小操作数
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

print(dp[-1][-1])