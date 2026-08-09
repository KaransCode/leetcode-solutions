class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]* n for _ in range(n)]
        top = 0 ; left = 0
        bottom = right = n - 1
        value = 1
        while top <= bottom:
            # Right
            for i in range(left,right+1):
                matrix[left][i] = value
                value +=1
            top += 1
            
                
            # Bottom
            for i in range(top,bottom+1):
                matrix[i][right] = value
                value +=1
            right -= 1

            # Left
            for i in range(right,left-1,-1):
                matrix[bottom][i] = value
                value +=1
            bottom -= 1

            # Top
            for i in range(bottom, top-1,-1):
                matrix[i][left] = value
                value +=1
            left += 1
        return matrix

"""
        matrix = [[0]* n for _ in range(n)]
        top = 0 ; left = 0
        rows = len(matrix); cols = len(matrix[0])
        bottom = rows - 1; right = cols - 1
        value = 1
        while top <= bottom:
            # Right
            for i in range(left,right+1):
                matrix[left][i] = value
                value +=1
            top += 1
              
            # Bottom
            for i in range(top,bottom+1):
                matrix[i][right] = value
                value +=1
            right -= 1

            if left <= right:  
                # Left
                for i in range(right,left-1,-1):
                    matrix[bottom][i] = value
                    value +=1
                bottom -= 1

            if top <= bottom:
                # Top
                for i in range(bottom, top-1,-1):
                    matrix[i][left] = value
                    value +=1
                left += 1
        return matrix
"""