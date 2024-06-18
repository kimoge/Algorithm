nums = [1,2,3,1]


def getResult(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    # 两个的话更新不了，加上下行代码
    if len(dp) >= 2:
        dp[1] = max(nums[0], nums[1])

    for j in range(2, len(dp)):
        dp[j] = max(dp[j - 2] + nums[j], dp[j - 1])
    return dp


dp0 = getResult(nums[1:])
dp1 = getResult(nums[:-1])

print(max(dp0[-1], dp1[-1]))