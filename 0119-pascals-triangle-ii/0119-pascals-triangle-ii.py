class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 1:
            return [1] * (rowIndex + 1)
        
        lst = self.getRow(rowIndex - 1)
        new_lst = [1]

        for i in range(len(lst) - 1):
            new_lst.append(lst[i] + lst[i+1])
        
        new_lst.append(1)
        return new_lst
        
        