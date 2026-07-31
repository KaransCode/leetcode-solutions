class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            if m < len(nums1) or n < len(nums1):
                nums1[m+i] = nums2[i]
        nums1.sort()        