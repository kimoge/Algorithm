# 组合问题 回溯+剪枝操作
# 剪枝：当前的path + 之后剩余的长度 不够k，则直接减掉即可
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
    # # 剪枝方法1
    # if len(path) + len(list0) - start_index < k:
    #     return

    if k == len(path):
        arr.append(path.copy())  # 重点：python中必须使用copy函数，否则保存的path会改变
        return

    # 剪枝方法2
    # l = len(list0) - (k - len(path)) + 1
    # 将len(list0)更换为l即可完成剪枝
    for i in range(start_index, len(list0)):
    # for i in range(start_index, l):
         path.append(list0[i])
         back_tracking(list0, k, path, arr, i + 1)
         path.pop()


n = 5
nums = list(i for i in range(1, n+1))
print(nums)
arr = []
back_tracking(nums, 5, [], arr, 0)
print(arr)