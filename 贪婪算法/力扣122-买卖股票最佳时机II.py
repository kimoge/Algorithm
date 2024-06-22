prices = [7,1,5,3,6,4]

low = max(prices)
res = 0

for i in prices:
    # 截止目前为止最小值
    low = min(low, i)
    # 截止目前为止最大间距
    res = max(res, i - low)

print(res)
