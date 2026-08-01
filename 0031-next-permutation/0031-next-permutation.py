class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        break_point = -1; n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                break_point = i
                break
            
        if break_point == -1:
            nums.reverse()
            return nums
        
        for i in range(n-1,break_point,-1):
            if nums[i] > nums[break_point]:
                nums[break_point], nums[i] = nums[i], nums[break_point]
                break
                
        def reverseArray(arr, i,n):
            while i < n :
                arr[i], arr[n] = arr[n], arr[i]
                i+=1
                n-=1

        reverseArray(nums,break_point+1,n-1)