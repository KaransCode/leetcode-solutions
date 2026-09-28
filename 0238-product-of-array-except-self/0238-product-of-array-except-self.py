class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        prefixAndsuffix = 1
        for i in range(n):
            res[i] = prefixAndsuffix
            prefixAndsuffix *= nums[i]

        prefixAndsuffix = 1
        for i in range(n-1,-1,-1):
            res[i] *= prefixAndsuffix
            prefixAndsuffix *= nums[i]
        return res