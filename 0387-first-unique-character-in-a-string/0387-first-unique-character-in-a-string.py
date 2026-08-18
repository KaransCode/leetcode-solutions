class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = [0] * 26; index = 0
        for i in s:
            char[ord(i) - ord('a')] += 1
        
        for i in s:
            if char[ord(i) - ord('a')] == 1:
                return index  
            index += 1
        return -1