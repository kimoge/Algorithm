class Solution:
    def candy(self, ratings):
        res_left = [1] * len(ratings)
        res_right = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                res_left[i] = res_left[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res_right[i] = res_right[i + 1] + 1

        min_candy = 0
        for i in range(len(ratings)):
            min_candy += max(res_right[i], res_left[i])

        return min_candy

ratings= [1,2,87,87,87,2,1]
s = Solution()
s.candy(ratings)