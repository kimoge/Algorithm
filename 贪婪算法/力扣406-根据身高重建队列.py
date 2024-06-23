class Solution:
    def reconstructQueue(self, people):
        queue = sorted(people, key = lambda x: (-x[0], x[1]))
        print(queue)
        for i in range(len(queue)):
            index = queue[i][1]
            p = queue.pop(i)
            queue.insert(index, p)
        # print(queue)
        return queue

people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
s = Solution()
s.reconstructQueue(people)
