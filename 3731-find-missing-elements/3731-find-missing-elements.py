class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minimum = min(nums)
        maximum = max(nums)
        ans = []
        for num in range(minimum, maximum+1):
            if num not in nums:
                ans.append(num)
        return ans