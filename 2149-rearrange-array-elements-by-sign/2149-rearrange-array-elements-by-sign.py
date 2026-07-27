class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        n = len(nums)
        positive = 0; negative = 1; answer = [0] * n
        for num in nums:
            if num >= 0:
                answer[positive] = num
                positive += 2
            else:
                answer[negative] = num
                negative += 2
        return answer


        # positive = 0; negative = 0; answer = [0] * n
        # for num in nums:
        #     if num >= 0:
        #         answer[(2*positive)] = num
        #         positive += 1
        #     else:
        #         answer[(2*negative)+1] = num
        #         negative += 1
        # return answer