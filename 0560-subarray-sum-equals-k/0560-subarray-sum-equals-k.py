class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0; count = 0
        prefixSum = {}

        for num in nums:
            current_sum += num

            if current_sum == k:
                count += 1

            diff = current_sum - k
            if diff in prefixSum:
                count += prefixSum[diff]
            prefixSum[current_sum] = prefixSum.get(current_sum, 0) + 1
        return count

        # n = len(nums)
        # left = 0
        # current_sum = 0
        # numberOfSubArray = 0
        # for right in range(n):
        #     current_sum += nums[right]
        #     while current_sum > k and left < right:
        #         current_sum -= nums[left]
        #         left += 1
            
        #     if current_sum == k:
        #         numberOfSubArray += 1
        # return numberOfSubArray
        