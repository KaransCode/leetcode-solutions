class Solution:
    def findGCD(self, nums: List[int]) -> int:
            def smallest_greatest(nums):
                minimum = greatest = nums[0]
                for num in nums:
                    if num < minimum:
                        minimum = num
                    if num > greatest:
                        greatest = num
                return minimum, greatest
        
            def gcd(a,b):
                while b:
                    a,b = b,a%b
                return a
            
            a,b = smallest_greatest(nums)
            return gcd(a,b)