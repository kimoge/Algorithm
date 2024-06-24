class Solution:
    def partitionLabels(self, s):
        dic = dict()
        for i in range(len(s)):
            dic[s[i]] = i

        right = 0  # 右边界
        left = 0  # 左边界
        res = []
        for i in range(len(s)):
            right = max(right, dic[s[i]])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        print(res)
        return res


s = "ababcbacadefegdehijhklij"
so = Solution()
so.partitionLabels(s)
