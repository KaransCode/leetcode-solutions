class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        mostFrequent = -1
        max_frequency = -1
        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0)+1
            
        for key,value in freq.items():
            if value > max_frequency or value == max_frequency and key < mostFrequent:
                mostFrequent = key
                max_frequency = value
        return mostFrequent