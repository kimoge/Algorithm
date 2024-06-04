# 使用小顶堆实现，时间复杂度：nlogk
from collections import Counter
import heapq


nums = [1,1,1,2,2,3]
k = 2

pri_que = []  # 小顶堆
count = Counter(nums)
for num, times in count.items():
    # 默认构建小顶堆
    heapq.heappush(pri_que, (times, num))
    if len(pri_que) > k:
        heapq.heappop(pri_que)

# 以times从大到小输出
res = [num for _, num in pri_que[::-1]]
print(res)