import copy
n = 4  # n = 3无解
nums = [[0] * n for _ in range(n)]


def isTrue(nums, row, col):
    # 行是否合法
    for i in range(col):
        if nums[row][i] == 1:
            return False
    # 列是否合法
    for i in range(row):
        if nums[i][col] == 1:
            return False
    # 主对角线
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if nums[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # # 副对角线
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(nums):
        if nums[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def backtracking(arr, nums, n, row):
    if row == n:
        arr.append(copy.deepcopy(nums))
        return

    for col in range(n):
        if isTrue(nums, row, col):
            nums[row][col] = 1
            backtracking(arr, nums, n, row + 1)
            nums[row][col] = 0


arr = []
backtracking(arr, nums, n, 0)
print(arr)
for i in arr:
    for j in i:
        print(j)
    print()
