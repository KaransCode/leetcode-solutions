class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n; rightSum = [0]*n; answer = [0]*n
        leftSum[0] = 0
        rightSum[n-1] = 0
        for i in range(1,n):
            leftSum[i] = nums[i-1] + leftSum[i-1]
        for i in range(n-2,-1,-1):
            rightSum[i] = nums[i+1] + rightSum[i+1]
        
        for i in range(n):
            answer[i] = abs(rightSum[i] - leftSum[i])
        return answer