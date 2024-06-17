# 分割等和子集的变体：stones分割两部分，使差最小， 参照分割等和子集


def getResult(stones):
    target = sum(stones) // 2
    dp = [0] * (target+1)

    for i in range(len(stones)):
        for j in range(len(dp)-1, stones[i] - 1, -1):
            # if j >= stones[i]:
            dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

    print(sum(stones) - 2 * dp[target])
    # print("sum:", sum(stones))
    # for i in dp:
    #     print(i, end = " ")


stones = [2,7,4,1,8,1]
getResult(stones)