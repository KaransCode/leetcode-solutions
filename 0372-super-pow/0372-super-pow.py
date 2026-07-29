class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def mod(a,n,M):
            if n == 0:
                return 1
            elif n%2 == 0:
                y = mod(a,n//2,M)
                return (y*y)%M
            else:
                return (((a%M) * mod(a,n-1,M))%M)

        M = 1337
        n = ""
        for i in b:
            n += str(i)
        n = int(n)

        result = mod(a,n,M)
        return result