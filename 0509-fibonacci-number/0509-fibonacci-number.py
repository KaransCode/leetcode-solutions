class Solution:
    def fib(self, n: int) -> int:

# Recursion with Memoization
        memo = [-1] * (n+1)
        memo[0] = 0
        if n >= 1:
            memo[1] = 1

        def helper(k):
            if memo[k] != -1:
                return memo[k]
            memo[k] = helper(k-1) + helper(k-2)
            return memo[k]
        return helper(n)

# Iterative Approach 

        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        
        # prev1 = 0
        # prev2 = 1

        # for _ in range(2,n+1):
        #     current = prev1 + prev2
        #     prev1, prev2 = prev2, current
        # return prev2 