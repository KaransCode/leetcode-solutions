class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        n = len(nums)
        monotoneIncreasing = True
        monotoneDecreasing = True

        for i in range(n-1):
            if not (nums[i] <= nums[i+1]):
                monotoneIncreasing = False

            if not (nums[i] >= nums[i+1]):
                monotoneDecreasing = False

        return monotoneIncreasing or monotoneDecreasing      