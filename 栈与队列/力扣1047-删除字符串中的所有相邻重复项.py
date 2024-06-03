s = "abbaca"


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in s:
            if not stack or i != stack[-1]:
                stack.append(i)
            elif stack[-1] == i:
                stack.pop()

        return ("".join(stack))

o = Solution()
print(o.removeDuplicates(s))

