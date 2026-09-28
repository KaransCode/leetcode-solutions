class Solution:
    def maxDepth(self, s: str) -> int:
        if s == "":
            return 0
        count = 0
        maxCount = 0
        for char in s:
            if char == "(":
                count += 1
                maxCount = max(maxCount, count)
            elif char == ")":
                count -= 1
        return maxCount