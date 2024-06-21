# 与接雨水类似，只是栈的增减顺序不同，以及前后位置插入0
heights = [2,4]
# 前后都插入0
heights.insert(0, 0)
heights.append(0)
res = 0
# 单调栈存放heights下标
stack = []
stack.append(0)

for i in range(1, len(heights)):
    if heights[i] > heights[stack[-1]]:
        stack.append(i)
    elif heights[i] == heights[stack[-1]]:
        stack.pop()
        stack.append(i)
    else:
        while stack and heights[i] < heights[stack[-1]]:
            mid = stack.pop()
            if stack:
                # 此次循环不pop得left
                left = stack[-1]
                h = heights[mid]
                w = i - left - 1
                res = max(h * w, res)
        stack.append(i)

print(res)