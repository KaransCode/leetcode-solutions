class Solution:
    def myPow(self, x: float, n: int) -> float:
        exponent = n
        n = abs(n)
        answer = 1.0
        while n > 0:
            if n%2 == 0:
                n //= 2
                x *= x
            else:
                answer *= x
                n -= 1
                
        if exponent < 0:
            answer = (1/answer)

        return answer