class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        points.sort(key = lambda x: (x[0]))
        # print(points)
        res = 1
        for i in range(1, len(points)):
            if points[i - 1][1] < points[i][0]:
                res += 1
            else:
                points[i][1] = min(points[i][1], points[i - 1][1])
        # print(res)
        return res


points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
s = Solution()
s.findMinArrowShots(points)