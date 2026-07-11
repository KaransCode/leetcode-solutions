class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversedNum = 0
        copy = x
        while x > 0:
            lastDigit = x%10
            reversedNum = (reversedNum * 10) + lastDigit
            x //= 10
        return copy == reversedNum