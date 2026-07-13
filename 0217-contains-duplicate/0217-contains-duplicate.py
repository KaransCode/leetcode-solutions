# from collections import defaultdict
# from collections import Counter

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

        # frequency = defaultdict(int)
        # for num in nums:
        #     frequency[num] += 1
        # for key, value in frequency.items():
        #     if value > 1 :
        #         return True
        # return False

        numberSet = set(nums)
        return len(numberSet) < len(nums)