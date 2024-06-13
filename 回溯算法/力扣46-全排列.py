# 无重复元素
nums = [1, 2, 3]
used = [0] * len(nums)


def backtracking(nums, arr, path, used):
    if len(path) == len(nums):
        arr.append(path)

    for i in range(len(nums)):
        if used[i] != 1:
            used[i] = 1
            backtracking(nums, arr, path + [nums[i]], used)
            used[i] = 0


arr = []
backtracking(nums, arr, [], used)
print(arr)