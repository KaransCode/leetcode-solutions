class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = rowIndex + 1
        answer = 1; rowList = [1]
        for i in range(1,row):
            answer = answer * (row-i)
            answer = answer // i
            rowList.append(answer)
        return rowList