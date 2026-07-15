class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # sumOfodd = n * n
        # sumOfeven = n * (n+1)

        # a = sumOfeven
        # b = sumOfodd
        # while b != 0:
        #     temp_b = b
        #     b = a % b
        #     a = temp_b
        # return a
        return n