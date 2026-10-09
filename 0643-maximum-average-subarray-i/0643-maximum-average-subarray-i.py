class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        left = 0
        maxAvg = float('-inf')
        currentSum = 0.0
        currentAvg = 0.0

        for right in range(n):
            currentSum += nums[right]
            window = right - left + 1
            if window == k:
                currentAvg = currentSum / k
                maxAvg = max(maxAvg, currentAvg)

                currentSum -= nums[left]
                left += 1
        return maxAvg