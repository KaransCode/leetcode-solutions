class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        memo[0] = memo[1] = 1
        if n < 2:
            return 1
        
        def helper(k):
            if memo[k] != -1:
                return memo[k]
            memo[k] = helper(k-1) + helper(k-2)
            return memo[k]
        return helper(n)

# Recursive Approach
        # if n == 0 or n == 1:
        #     return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)