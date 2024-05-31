# 两个两个放入map（nums1[i]+nums[j]：times），减少时间复杂度
nums1 = [-1, -1]
nums2 = [-1, 1]
nums3 = [-1, 1]
nums4 = [1, -1]


dic0 = dict()
for i in nums1:
    for j in nums2:
        if i + j in dic0:
            dic0[i + j] += 1
        else:
            dic0[i + j] = 1

dic1 = dict()
for i in nums3:
    for j in nums4:
        if i + j in dic1:
            dic1[i + j] += 1
        else:
            dic1[i + j] = 1

res = 0
for i in dic0.keys():
    if -i in dic1.keys():
        res += dic0[i] * dic1[-i]

print(res)




