class Solution:
    def pascalsRow(self,row):
        answer = [1]; r = 1
        for col in range(1,row):
            r *= row - col
            r //= (col)
            answer.append(r)
        return answer

    def generate(self, numRows: int) -> List[List[int]]:
        result = []; n = numRows
        for i in range(1,n+1):
            result.append(self.pascalsRow(i))
        return result