# 1、dp[j]:0~j范围最大价值dp[j]
# 2、dp[j] = max(dp[j-1], dp[j-2] + nums[j]) # 不考虑物品i；考虑物品i
# 3、遍历顺序：左到右
# 4、初始化：dp[0]、dp[1]根据nums初始化

nums = [2, 1]

dp = [0] * len(nums)
dp[0] = nums[0]
# 两个的话更新不了，加上下行代码
if len(dp) >= 2:
    dp[1] = max(nums[0], nums[1])

for j in range(2, len(dp)):
    dp[j] = max(dp[j - 2] + nums[j], dp[j - 1])
print(dp)