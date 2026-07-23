class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        limit = min(a,b)
        count = 0
        for i in range(1, limit+1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count

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