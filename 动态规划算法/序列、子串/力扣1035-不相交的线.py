# 就是求最长公共子序列（可以不连续）

nums1 = [1,4,2]
nums2 = [1,2,4]

dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

for i in range(1, len(nums1) + 1):
    for j in range(1, len(nums2) + 1):
        if nums1[i - 1] == nums2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# print(dp)
print(dp[-1][-1])