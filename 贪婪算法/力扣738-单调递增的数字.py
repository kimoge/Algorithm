class Solution:
    def monotoneIncreasingDigits(self, n):
        str_n = list(str(n))
        # print(str_n)
        flag = len(str_n)
        for i in range(len(str_n)-1, 0, -1):
            if str_n[i] < str_n[i - 1]:
                flag = i
                str_n[i - 1] = str(int(str_n[i - 1]) - 1)

        for i in range(flag, len(str_n)):
            str_n[i] = "9"
        # print(str_n)

        return int("".join(str_n))


n = 777616726
s = Solution()
s.monotoneIncreasingDigits(n)
