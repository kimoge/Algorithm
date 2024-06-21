# 思路：和每日温度类似，只是遍历nums2，判断元素再nums1的话更改对应位置结果
nums1 = [4,1,2]
nums2 = [1,3,4,2]

res = [-1] * len(nums1)
# 便于修改res的map集合 nums1元素值：nums1_index
map = dict()
for i in range(len(nums1)):
    map[nums1[i]] = i

stack = []
stack.append(nums2[0])
for i in range(1, len(nums2)):
    if stack[-1] >= nums2[i]:
        stack.append(nums2[i])
    else:
        while stack and stack[-1] < nums2[i]:
            temp = stack.pop()
            if temp in map.keys():
                res[map[temp]] = nums2[i]
        stack.append(nums2[i])

print(res)