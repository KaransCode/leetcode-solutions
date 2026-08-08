class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        
        # Transpose of Matrix
        for i in range(size-1):
            for j in range(i+1, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse the Rows
        for i in range(size):
            matrix[i].reverse()