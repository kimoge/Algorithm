# set集合
nums1 = [1,2,2,1]
nums2 = [2,2]

# res = []
# set0 = set(nums1)
# for i in nums2:
#     if i in set0:
#         res.append(i)
#         set0.remove(i)
# print(res)

print(list(set(nums1)&set(nums2)))
