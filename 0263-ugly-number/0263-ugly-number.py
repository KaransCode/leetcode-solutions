class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        UglyNumbers = [2,3,5]
        
        for factors in UglyNumbers:
            while n% factors== 0:
                n //= factors
        return n == 1