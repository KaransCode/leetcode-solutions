class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))

        
        # size = len(matrix)
        # for rows in range(size-1):
        #     for col in range(rows+1, size):
        #         matrix[rows][col], matrix[col][rows] = matrix[col][rows],matrix[rows][col]
        # return matrix