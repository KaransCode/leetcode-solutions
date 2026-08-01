class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1); n = len(word2)
        i = j = 0; result = []
        
        while i < m and j < n:
            result.append(word1[i])
            result.append(word2[i])
            i += 1
            j += 1
        
        while i < m:
            result.append(word1[i])
            i += 1
            
        while i < n:
            result.append(word2[i])
            i += 1
            
        return "".join(result)