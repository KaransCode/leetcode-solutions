class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hashSet = set()
        result = 1; count = 0
        
        for num in nums:
            hashSet.add(num)
        
        for num in hashSet:
            if num - 1 not in hashSet:
                count = 1
                x = num
                while x + 1 in hashSet:
                    x += 1
                    count += 1
            result = max(result, count)
        return result

## Brute Force
        # def linearsearch(target,nums=nums):
        #     if not nums:
        #         return 0
        #     if target in nums:
        #         return 1
        #     else:
        #         return 0
        
        # result = 1
        # for num in range(len(nums)):
        #     x = nums[num]
        #     count = 1
        #     while (linearsearch(x+1) == 1):
        #         x += 1
        #         count += 1
        #     result = max(count, result)
        # return result
    
# Better
        # count = 0; largest = 1
        # last_smaller = float('-inf')
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i]-1 == last_smaller:
        #         count += 1
        #         last_smaller = nums[i]
        #     elif nums[i] != last_smaller:
        #         count = 1
        #         last_smaller = nums[i]
        #     largest = max(count, largest)
        # return largest