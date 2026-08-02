class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set()
        n = max(nums)
        for num in nums:
            numSet.add(num)

        # limit = 2**31
        limit = abs(max(nums))
        for i in range(1,limit+2):
            if i not in numSet:
                return i