class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = [ ]
        res = 0

        for parenthes in s:
            if parenthes == "(":
                stack.append(parenthes)
            else:
                if stack:
                    stack.pop()
                else:
                    res += 1
        return res + len(stack)