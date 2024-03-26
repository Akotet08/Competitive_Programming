class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        col, row = len(matrix[0]), len(matrix)
        self.m = [[0] * (col + 2) for _ in range(row + 2)]
        for i in range(row):
            for j in range(col):
                self.m[i+1][j+1] = self.m[i][j+1] + self.m[i+1][j] - self.m[i][j] + matrix[i][j]
        
        print(self.m)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sub1 = self.m[row1][col2 + 1]
        sub2 = self.m[row2 + 1][col1]
        add1 = self.m[row1][col1]
        return self.m[row2 + 1][col2+1] - sub1 - sub2 + add1
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)