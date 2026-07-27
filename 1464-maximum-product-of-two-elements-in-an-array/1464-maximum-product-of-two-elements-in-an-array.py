class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 
        nums.sort()
        return ((nums[-1]-1) * (nums[-2]-1))
        