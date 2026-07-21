class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # countDict = {}
        # for i in nums:
        #     countDict[i] = countDict.get(i,0)+1
        # majority = max(countDict, key=countDict.get)
        # return majority if majority >= majority else -1

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