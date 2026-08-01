class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        nums1 = nums.copy()
        nums.reverse()
        print(nums1, nums, type(nums1), type(nums))
        return nums1 + nums