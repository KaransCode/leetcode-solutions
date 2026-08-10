import numpy as np
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        totalElement = len(original); actualElement = m*n
        answer = [[0]*n for _ in range(m)]
        if totalElement != actualElement:
            return []
        
        for row in range(totalElement):
            answer[row//n][row%n] = original[row]
        return answer
        