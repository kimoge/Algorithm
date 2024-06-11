# 组合中可能有重复元素，需要去重
nums = [10, 1, 2, 7, 6, 1, 5]
target_sum = 7
# 一定要先排序，为后面去重做准备
nums.sort()
used = [0] * len(nums) # 用于剪枝去重
# print(nums)


def backtracking(nums, target_sum, path, path_sum, arr, start_index, used):
    if target_sum == path_sum:
        arr.append(path)
        return
    elif target_sum < path_sum:
        return

    for i in range(start_index, len(nums)):
        if i !=0:
            # 树层去重:如果有重复元素且之前的重复元素没有使用，则剪该分枝
            if nums[i] == nums[i-1] and used[i-1] == 0:
                continue

        # 正常分支处理
        used[i] = 1
        if len(path) == 0:
            backtracking(nums, target_sum, path+[nums[i]], nums[i], arr, i + 1, used)
        else:
            backtracking(nums, target_sum, path+[nums[i]], sum(path) + nums[i], arr, i + 1, used)
        used[i] = 0


arr = []
backtracking(nums, target_sum, [], 0, arr, 0, used)
print(arr)