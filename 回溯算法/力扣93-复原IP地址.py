class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        self.backtracking(s, 0, 0, [], res)
        return (res)

    def backtracking(self, s, startindex, level, path, res):
        """
        startindex:endindex------左闭右开
        """
        if level == 4 and startindex == len(s):
            res.append(".".join(path))
            return

        for i in range(startindex + 1, len(s)+1):
            if self.isValue(s, startindex, i):
                path.append(s[startindex:i])
                self.backtracking(s, i, level + 1, path, res)
                path.pop()
            else:
                break

    def isValue(self, s, start, end):
        try:

            s_int = int(s[start:end])
            if end - start != len(str(s_int)):
                return False
            if 0 > s_int or s_int > 255:
                return False
            return True
        except:
            return False


so = Solution()
s = "25525511135"
print(so.restoreIpAddresses(s))