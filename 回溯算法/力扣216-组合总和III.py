def back_tracking(res, k, path, arr, start_index):
    """
    回溯算法解决组合总和
    :param res: 还需要的剩余数
    :param k: 需要多少个数
    :param path: 每层存入的一维列表结果
    :param arr: 二维列表结果
    :param start_index: 初始位置
    :return: 空
    """
    # 满足条件，收集结果返回
    if len(path) == k and res == 0:
        arr.append(path.copy())
        return
    # 此路不通，返回，其实包含了剪枝操作
    elif res < 0:
        return

    for i in range(start_index, 10):
        path.append(i)
        back_tracking(res-i, k, path, arr, i+1)
        path.pop()


# [1,9]范围内k个不重复数和为n的组合
n = 9
k = 3
arr = []
back_tracking(n, k, [], arr, 1)
print(arr)

