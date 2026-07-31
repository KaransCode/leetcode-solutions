class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = max(nums)
        for num in nums:
            if abs(num) < abs(closest):
                closest = num
            
            if abs(num) == abs(closest):
                if closest < num:
                    closest = num
                
        return closest
        