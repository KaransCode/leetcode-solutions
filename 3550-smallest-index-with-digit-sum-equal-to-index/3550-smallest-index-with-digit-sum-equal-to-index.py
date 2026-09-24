class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumOfDigit(num):
            DigitSum = 0
            while num:
                lastDigit = num%10
                DigitSum += lastDigit
                num //= 10
            return DigitSum
        
        for i in range(len(nums)):
            if i == sumOfDigit(nums[i]):
                return i
        return -1     