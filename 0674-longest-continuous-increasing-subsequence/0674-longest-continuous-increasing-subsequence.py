class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return
        result = 1
        maxcontinous = 1
        for num in range(1,len(nums)):
            if nums[num] > nums[num-1]:
                result += 1
            else:
                result = 1
            maxcontinous = max(maxcontinous, result)
        return maxcontinous