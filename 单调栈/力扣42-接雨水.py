height = [0,1,0,2,1,0,1,3,2,1,2,1]

res = 0
# 单调栈存放height下标
stack = []
stack.append(0)

for i in range(1, len(height)):
    # case1:不是右边第一个高的，直接加入
    if height[i] < height[stack[-1]]:
        stack.append(i)
    # case2:高度相同，替换掉
    elif height[i] == height[stack[-1]]:
        stack.pop()
        stack.append(i)
    # case3:找到凹槽，计算雨水高度
    else:
        while stack and height[i] > height[stack[-1]]:
            mid = stack.pop()
            if stack:
                # 此次循环不pop得left
                left = stack[-1]
                h = min(height[left], height[i]) - height[mid]
                w = i - left - 1
                res += h * w
        stack.append(i)

print(res)