class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        result = 0
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num,0) + 1
        
        for key, value in frequency.items():
            if value == 2:
                result ^= key
        return result
        