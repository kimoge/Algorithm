g = [10,9,8,7]
s = [5,6,7,8]


class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
            j += 1
        return count


so = Solution()
print(so.findContentChildren(g, s))