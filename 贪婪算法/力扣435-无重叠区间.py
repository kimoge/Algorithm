class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        res = 0  # 重叠区间个数
        end = intervals[0][1]  # 区间分割点
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                end = intervals[i][1]
            else:
                res += 1
                end = min(intervals[i][1], end)
        return res


intervals = [[1, 100], [1, 11], [2, 12], [11, 22]]
s = Solution()
s.eraseOverlapIntervals(intervals)