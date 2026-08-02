class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set()
        n = max(nums)
        for num in nums:
            numSet.add(num)

        limit = 2**31
        for i in range(1,limit):
            if i not in numSet:
                return i