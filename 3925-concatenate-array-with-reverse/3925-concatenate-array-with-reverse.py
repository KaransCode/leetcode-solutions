class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        nums1 = nums[::-1]
        return nums + nums1