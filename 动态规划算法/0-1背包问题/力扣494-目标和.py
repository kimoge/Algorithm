# 参考分割等和子集
# 加法集：[+]
# 减法集：[-]
# [+] + [-] = sum(nums)
# [+] - [-] = target
# sum(nums)、target已知，求一个加法集或减法集即可。

# 1、dp[j]：装满容量为j的背包的方法个数dp[j]个
# 2、dp[j] += dp[j-num[i]] i:0~...
# 3、初始化全为0
# 4、遍历顺序：左到右


def getResult(nums, target):
    # [100], -100
    if len(nums) == 1 and abs(nums[0]//target) != 1:
        return 0

    if (sum(nums) + target) % 2 != 0:
        return 0

    res = (sum(nums) + target) // 2
    # [100, 100] -400
    if res < 0:
        return 0

    dp = [0] * (res + 1)
    dp[0] = 1

    for i in range(len(nums)):
        for j in range(len(dp) - 1, nums[i] - 1, -1):
            # if j >= nums[i]:
            dp[j] += dp[j - nums[i]]
    # print(dp)
    return dp[res]


nums = [1000]
target = -1000
res = getResult(nums, target)
print(res)