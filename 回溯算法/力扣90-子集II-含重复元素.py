nums = [1, 2, 2]
nums.sort()
used = [0] * len(nums)


def backtracking(arr, used, path, start_index):
    arr.append(path)

    for i in range(start_index, len(nums)):
        if i > 0:
            if nums[i] == nums[i-1] and used[i-1] == 0:
                continue
        used[i] = 1
        backtracking(arr, used, path + [nums[i]], i + 1)
        used[i] = 0


arr = []
backtracking(arr, used, [], 0)
print(arr)
