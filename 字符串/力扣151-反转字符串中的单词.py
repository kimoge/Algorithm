def myReverse(s_l, l, r):
    while l < r:
        temp = s_l[l]
        s_l[l] = s_l[r]
        s_l[r] = temp
        l += 1
        r -= 1


s = " hello world  "
s_l = list(s)

# 双指针消除空格
low = 0
fast = 0
length = len(s_l)
while fast < len(s_l):
    # 找到要填充目标
    if s_l[fast] != " ":
        # 如果慢指针不在首位，先添加一个空格，长度+1
        if low != 0:
            s_l[low] = " "
            low += 1
            length += 1
        # 持续赋值一个单词
        while fast < len(s_l) and s_l[fast] != " ":
            s_l[low] = s_l[fast]
            low += 1
            fast += 1

    else:
        # 遇见空格，长度-1
        length -= 1
        fast += 1
# print(s_l[:length])

myReverse(s_l, 0, length-1)

l = 0
r = 0
# 左闭右开字符串
while r <= length:
    if r == length or s_l[r] == " ":
        myReverse(s_l, l, r-1)
        r += 1
        l = r
    r += 1

print("".join(s_l[:length]))

