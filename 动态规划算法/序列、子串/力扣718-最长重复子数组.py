# 1、dp[i][j]:以下标i-1结尾的nums1和以下标j-1结尾的nums2的最长重复子数组（连续）
# 2、if nums1[i-1] == nums[j-1]: dp[i][j] = dp[i-1][j-1] + 1
# 3、dp第一行第一列初始化为0
# 4、从左到右，从上到下
# 5、打印dp

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

dp = [[0] * (len(nums2) + 1) for _ in range((len(nums1) + 1))]
res = 0

for i in range(1, len(nums1) + 1):
    for j in range(1, len(nums2) + 1):
        if nums1[i-1] == nums2[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        res = max(res, dp[i][j])

print(dp)
print(res)