class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        check_row = set()
        check_col = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    check_row.add(i)
                    check_col.add(j)
        
        for i in range(row):
            for j in range(col):
                if i in check_row or j in check_col:
                    matrix[i][j] = 0
        