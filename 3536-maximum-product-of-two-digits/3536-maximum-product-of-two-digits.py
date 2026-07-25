class Solution:
    def maxProduct(self, n: int) -> int:
        if n <= 0:
            return 0
        max_product = 0
        result = [int(i) for i in str(n)]
        result.sort()
        max_product = result[-1] * result[-2]
        return max_product