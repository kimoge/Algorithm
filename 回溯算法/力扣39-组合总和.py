nums = [2, 5, 3]
sum_nums = 4
# nums中无重复元素，元素组合为sum的情况，元素可重复使用


def backtracking(nums, path, s, arr, start_index):
    if len(path) > 0:
        if sum(path) == s:
            arr.append(path.copy())
            return
        elif sum(path) > s:
            return
    # 加入start_index是因为避免组合的重复结果
    for i in range(start_index, len(nums)):
        path.append(nums[i])
        backtracking(nums, path, s, arr, i)
        path.pop()


arr = []
backtracking(nums, [], sum_nums, arr, 0)
print(arr)