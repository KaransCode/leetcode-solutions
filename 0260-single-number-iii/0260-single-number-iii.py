class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num,0) + 1
            
        for key, value in freq.items():
            if value == 1:
                result.append(key)
        return result