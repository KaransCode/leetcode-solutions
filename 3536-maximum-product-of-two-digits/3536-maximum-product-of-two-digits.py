class Solution:
    def maxProduct(self, n: int) -> int:
        if n <= 0:
            return 0
        max1 = max2 = 0
        for digit in str(n):
            num = int(digit)

            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return max1 * max2
