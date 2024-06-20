# 与求最长公共子序列类似，区别是只能删除t元素

s = "abc"
t = "ahbgdc"

dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

for i in range(1, len(t) + 1):
    for j in range(1, len(s) + 1):
        if s[j-1] == t[i-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = dp[i-1][j]

print(dp)
print(dp[-1][-1] == len(s))