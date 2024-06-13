nums = [1, 2, 2]
used = [0] * len(nums)  # 树枝去重


def backtracking(arr, nums, path, used):
    if len(nums) == len(path):
        arr.append(path)

    set0 = set()  # 树层去重
    for i in range(len(nums)):
        if used[i] != 1 and nums[i] not in set0:
            used[i] = 1
            backtracking(arr, nums, path + [nums[i]], used)
            used[i] = 0
            set0.add(nums[i])


arr = []
backtracking(arr, nums, [], used)
print(arr)