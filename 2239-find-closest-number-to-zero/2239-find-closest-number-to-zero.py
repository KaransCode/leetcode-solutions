class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        if not nums:
            return 
        closest = float("inf")
        for num in nums:
            if abs(num) < abs(closest):
                closest = num
            
            if abs(num) == abs(closest):
                if closest < num:
                    closest = num      
        return closest