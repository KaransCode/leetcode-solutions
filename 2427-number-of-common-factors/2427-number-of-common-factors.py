class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        #1 using GCD
        def gcd(a,b):
            while b:
                a,b = b, a % b
            return a
        g = gcd(a,b)

        count = 0
        i = 1
        while i*i <= g:
            if g % i == 0:
                if g == i*i:
                    count += 1
                else:
                    count += 2
            i += 1
        return count


        #  Using min. limit for loop 
        # limit = min(a,b)
        # count = 0
        # for i in range(1, limit+1):
        #     if a % i == 0 and b % i == 0:
        #         count += 1
        # return count

        # Using Set and intersection
        
        # factors_a = set()
        # factors_b = set()
        # factors_a.add(1); factors_a.add(a)
        # factors_b.add(1); factors_b.add(b)
        # squarerootOfa = a**0.5; squarerootOfa = int(squarerootOfa)
        # squarerootOfb = b**0.5; squarerootOfb = int(squarerootOfb)
        # for i in range(1, squarerootOfa+3):
        #     if a % i == 0:
        #         factors_a.add(i)
        #         if i != squarerootOfa:
        #             factors_a.add(a//i)
                    
        # for i in range(1, squarerootOfb+3):
        #     if b % i == 0:
        #         factors_b.add(i)
        #         if i != squarerootOfb:
        #             factors_b.add(b//i)
        # commonfactors = factors_a.intersection(factors_b)
        # return len(commonfactors)   