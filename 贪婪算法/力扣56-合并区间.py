class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # 无包含，则加入结果
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            # 包含，更新结果最后一个区间的右边界
            else:
                res[-1][1] = max(intervals[i][1], res[-1][1])

        print(res)
        return res


intervals = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
s.merge(intervals)