class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stringlist = s.split()
        return len(stringlist[-1])