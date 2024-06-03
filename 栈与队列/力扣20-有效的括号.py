s = "()[]{}"


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            elif len(stack) == 0 or stack[-1] != i:
                return(False)
            else:
                stack.pop()

        return len(stack) == 0