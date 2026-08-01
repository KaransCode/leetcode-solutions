class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        mid = -1; n = len(nums)
        for i in range(n):
            leftSide = sum(nums[:i]); rightSide = sum(nums[i+1:])
            if leftSide == rightSide:
                return i  
        return mid 
        