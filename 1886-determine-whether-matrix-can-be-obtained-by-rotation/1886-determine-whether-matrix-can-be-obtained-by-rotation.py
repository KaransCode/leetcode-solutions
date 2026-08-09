class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        result = False
        def rotateMatrix(matrix):
            size = len(matrix)
            for i in range(size-1):
                for j in range(i+1, size):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            for i in range(size):
                matrix[i].reverse()
        
        # Checking Rotation
        rotation = 4
        for _ in range(rotation):
            rotateMatrix(mat)
            if mat == target:
                return True
        return result
        