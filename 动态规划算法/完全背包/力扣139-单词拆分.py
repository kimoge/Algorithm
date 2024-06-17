# 1、dp[j]:长度为j的背包是否能由单词装满：dp[j]:True or False
# 2、dp[j] = dp[j - len(wordict[i])] and isInWordDict(wordDict, s[j - len(wordict[i]) : j])
# 3、初始化：dp[0] = True
# 4、遍历顺序:先背包后物品：排列数
# 5、打印
s = "applepenapple"
wordDict = ["apple", "pen"]

dp = [False for i in range(len(s) + 1)]
dp[0] = True


def isInWordDict(wordDict, s):
    if s in wordDict:
        return True
    return False


for j in range(len(dp)):
    for i in range(len(wordDict)):
        if j >= len(wordDict[i]):
            dp[j] = dp[j - len(wordDict[i])] and isInWordDict(wordDict, s[j-len(wordDict[i]):j])
            if dp[j]:
                break

print(dp)
# print(dp[-1])