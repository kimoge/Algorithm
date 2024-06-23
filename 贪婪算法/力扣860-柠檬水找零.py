class Solution:
    def lemonadeChange(self, bills):
        dic = {5: 0, 10: 0}
        for money in bills:
            if money == 5:
                dic[money] += 1
            elif money == 10:
                if dic[5] >= 1:
                    dic[5] -= 1
                    dic[10] += 1
                else:
                    return False
            else:
                if dic[10] >= 1 and dic[5] >= 1:
                    dic[10] -= 1
                    dic[5] -= 1
                elif dic[5] >= 3:
                    dic[5] -= 3
                else:
                    return False
        return True
