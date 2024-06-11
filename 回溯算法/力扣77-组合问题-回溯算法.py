# 组合问题
n = 5
nums = list(i for i in range(1, n+1))
print(nums)


def back_tracking(list0, k, path, arr, start_index):
    """
    回溯算法解决组合问题
    :param list0: 要查找的元素列表
    :param k: 需要的组合大小
    :param path: 存结果的一维列表
    :param arr: 存一维结果的二维列表
    :param start_index: 查找的初始位置
    :return: 空
    """
    if k == len(path):
        arr.append(path.copy())  # 重点：python中必须使用copy函数，否则保存的path会改变
        return

    for i in range(start_index, len(list0)):
         path.append(list0[i])
         back_tracking(list0, k, path, arr, i + 1)
         path.pop()


arr = []
back_tracking(nums, 2, [], arr, 0)
print(arr)