class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
                
        for i in range(10):
            current = n + i
            result = 1
            temp = current
            while temp:
                lastDigit = temp%10
                result *= lastDigit
                temp//=10

                if result == 0:
                    break
            
            if result % t == 0:
                return current
   
        return -1