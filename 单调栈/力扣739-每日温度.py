temperatures = [73,74,75,71,69,72,76,73]


# 暴力解法
# answer = []
#
# for i in range(len(temperatures)):
#     temp = 0
#     for j in range(i+1, len(temperatures)):
#         if temperatures[j] > temperatures[i]:
#             temp = j - i
#             break
#     answer.append(temp)
#
# print(answer)

# 单调栈
res = [0] * len(temperatures)
stack = []  # 存放便利过的元素
stack.append(0)
for i in range(1, len(temperatures)):
    # 没有找到比遍历过得栈首元素大的
    if temperatures[stack[-1]] >= temperatures[i]:
        stack.append(i)
    else:
        # 找到比栈首元素大的
        while stack and temperatures[stack[-1]] < temperatures[i]:
            temp = stack.pop()
            res[temp] = (i - temp)
        stack.append(i)
print(res)