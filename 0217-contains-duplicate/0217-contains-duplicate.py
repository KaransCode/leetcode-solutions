# from collections import Counter
from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # frequency = {}
        # for num in nums:
        #     frequency[num] = frequency.get(num, 0) + 1
        # for key, value in frequency.items():
        #     if value > 1 :
        #         return True
        # return False

        # frequency = Counter(nums)
        # for key, value in frequency.items():
        #     if value > 1 :
        #         return True
        # return False

        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        for key, value in frequency.items():
            if value > 1 :
                return True
        return False