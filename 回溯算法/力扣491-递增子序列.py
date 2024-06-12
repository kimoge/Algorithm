# notes:含有重复元素
nums = [4, 7, 6, 7]


def backtracking(nums, arr, path, start_index):
    if len(path) > 1:
        arr.append(path)

    # 为了本层去重
    map0 = dict()
    for i in set(nums):
        map0[i] = 0
    for i in range(start_index, len(nums)):
        if map0[nums[i]] == 1:
            continue
        if len(path) == 0 or path[-1] <= nums[i]:
            map0[nums[i]] = 1
            backtracking(nums, arr, path + [nums[i]], i + 1)


arr = []
backtracking(nums, arr, [], 0)
print(arr)


