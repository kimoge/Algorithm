nums = [1, 2, 3]


def backtracking(arr, nums, path, start_index):
    arr.append(path.copy())
    if start_index >= len(nums):
        return

    for i in range(start_index, len(nums)):
        backtracking(arr, nums, path + [nums[i]], i + 1)


arr = []
backtracking(arr, nums, [], 0)
print(arr)