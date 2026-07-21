class Solution:
    def sortColors(self, nums: List[int]) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums); red = white = 0; blue = n-1
        if n <= 1:
            return nums
        while white <= blue:
            if nums[white] == 0:
                nums[red],nums[white] = nums[white],nums[red]
                red += 1
                white += 1
            
            elif nums[white] == 1:
                white += 1

            else:
                nums[blue],nums[white] = nums[white],nums[blue]
                blue -= 1

        # 1st Approach
        # red = white = blue = 0
        # for num in nums:
        #     if num == 0:
        #         red += 1
        #     elif num == 1:
        #         white += 1
        #     else:
        #         blue += 1
        # for i in range(red):
        #     nums[i] = 0
        # for i in range(red, red+white):
        #     nums[i] = 1
        # for i in range(blue+white, len(nums)):
        #     nums[i] = 2
        
        # return nums

        # n = len(nums)
        # low = 0
        # high = n - 1
        # mid = low + (low+high)//2

        #  2nd Approach

        # while low < high:
        #     if nums[mid] < nums[low]:
        #         nums[low], nums[mid] = nums[mid], nums[low]
        #         low += 1
        #     elif nums[mid] > nums[high]:
        #         nums[high], nums[mid] = nums[mid], nums[high]
        #         high -= 1
        #     else:
        #         low += 1
        
        # return nums