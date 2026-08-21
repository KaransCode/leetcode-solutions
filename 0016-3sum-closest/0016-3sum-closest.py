class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest_sum = nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            left = i+1; right = n-1
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                temp = abs(target - temp_sum)
                check = abs(target - closest_sum)
                if temp < check:
                    closest_sum = temp_sum
                if temp_sum == target:
                    return temp_sum
                elif temp_sum > target:
                    right -= 1
                else:
                    left += 1
        return closest_sum