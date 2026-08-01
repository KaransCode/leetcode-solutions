class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1); n = len(word2)
        l = min(m,n)
        result = []
        for i in range(l):
            if i < m and i < n:
                result.append(word1[i])
                result.append(word2[i])
        result.extend(word2[l:])
        result.extend(word1[l:])
        final = "".join(result)
        return final
        