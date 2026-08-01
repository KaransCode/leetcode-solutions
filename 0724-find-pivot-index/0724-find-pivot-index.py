class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = -1; n = len(nums);
        leftSide = [0]*n; rightSide = [0]*n; prefix_sum = suffix_sum = 0
        for i in range(n):
            prefix_sum += nums[i]
            leftSide[i] = prefix_sum
            
        for i in range(n-1,-1,-1):
            suffix_sum += nums[i]
            rightSide[i] = suffix_sum
        
        for i in range(n):
            if leftSide[i] == rightSide[i]:
                return i         
        return pivot