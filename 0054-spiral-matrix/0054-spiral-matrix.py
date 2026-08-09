class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        top = 0 ; left = 0
        rows = len(matrix); cols = len(matrix[0])
        bottom = rows - 1; right = cols - 1
        result = []
        
        while top <= bottom and left <= right:

            # Right
            for i in range(left,right+1):
                result.append(matrix[left][i])
            top += 1
            if top > bottom:
                break
                
            # Bottom
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right -= 1

            if left > right:
                break
            # Left
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom -= 1

            if top > bottom:
                break
            # Top
            for i in range(bottom, top-1,-1):
                result.append(matrix[i][left])
            left += 1
        return result