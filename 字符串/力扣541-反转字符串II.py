s = "abcdefg"
s_l = list(s)
k = 2


def myReverse(s_l, l, r):
    while l < r:
        temp = s_l[l]
        s_l[l] = s_l[r]
        s_l[r] = temp
        l += 1
        r -= 1


for i in range(0, len(s_l), 2*k):
    if i + k < len(s_l):
        myReverse(s_l, i, i + k - 1)
    else:
        myReverse(s_l, i, len(s_l) - 1)

print("".join(s_l))
