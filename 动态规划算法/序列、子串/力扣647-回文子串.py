# 大致思路：设置二维dp数组，确定dp数组中True的个数

# 1、dp[i][j]:s[i~j]（左闭右闭区间）是否为回文子串
# 2、if s[i] == s[j]:
#     case1:i==j: dp[i][j] = True
#     case2:abs(i - j) == 1: dp[i][j] = True
#     case3:if dp[i+1][j-1]: dp[i][j] = True
# 3、初始化：全为false
# 4、遍历顺序：左下->右上

s = "fdsklf"

dp = [[False]*len(s) for _ in range(len(s))]
res = 0

for i in range(len(s)-1, -1, -1):
    for j in range(i, len(s)):
        if s[i] == s[j]:
            if j - i <= 1 or dp[i+1][j-1]:
                dp[i][j] = True
                res += 1

print(res)