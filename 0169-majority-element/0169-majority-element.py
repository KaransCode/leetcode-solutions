class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            element = count = 0
            n = len(nums)
            for i in range(n):
                if count == 0:
                    element = nums[i]
                    count += 1
                elif element == nums[i]:
                    count += 1
                else:
                    count -= 1
            return element