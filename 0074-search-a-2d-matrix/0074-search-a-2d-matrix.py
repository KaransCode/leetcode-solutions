class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return 
        result = False 
        r = len(matrix); c = len(matrix[0])
        total = r * c
        low = 0 ; high = total - 1
        while low <= high:
            mid = low + (high - low)//2
            check = matrix[mid//c][mid%c]
            if target == check:
                return True
            elif target < check:
                high = mid - 1
            else:
                low = mid + 1
        return result