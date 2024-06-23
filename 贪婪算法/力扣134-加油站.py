class Solution:
    def canCompleteCircuit(self, gas, cost):
        # return self.method01(gas, cost)
        return self.method02(gas, cost)

    def method01(self, gas, cost):
        """
        暴力，超时
        """
        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            rest = gas[i] - cost[i]
            index = (i + 1) % len(gas)
            while rest > 0 and index != i:
                rest += gas[index] - cost[index]
                index = (index + 1) % len(gas)
            if rest >= 0 and index == i:
                return i
        return -1

    def method02(self, gas, cost):
        """
        贪心算法1
        """
        rest = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(rest) < 0:
            return -1

        index = 0
        cur_sum = 0
        for i in range(len(rest)):
            cur_sum += rest[i]
            if cur_sum < 0:
                cur_sum = 0
                index = i + 1

        return index