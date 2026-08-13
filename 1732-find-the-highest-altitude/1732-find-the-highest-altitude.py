class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = []
        curr_sum = 0; max_Sum = 0
        for i in range(len(gain)):
            answer.append(curr_sum)
            curr_sum += gain[i]
            max_Sum = max(max_Sum, curr_sum)
        return max_Sum