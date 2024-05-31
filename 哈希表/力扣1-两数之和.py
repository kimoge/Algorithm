# map字典结构
nums = [3,3]
target = 6

dic = dict()

res = []
for i, n in enumerate(nums):
    # 边加入边检查，可以避免map结构的重复元素缺陷
    if target - n in dic.keys():
        res = [dic[target - n], i]
        print(res)
        break
    dic[n] = i
