class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat) , len(mat[0]) 
        col = 0
        row = 0
        left = 0
        diag_up = 0
        diag_down = 0
        lst = [mat[0][0]]
        while row < n or col < m:
            # check if can go diagonally up
            if row - 1 >= 0 and col + 1 < m and (not diag_down):
                while row > 0 and col < m:
                    row -= 1
                    col += 1

                    if col < m and row < n:
                        # print('moving up:', mat[row][col])
                        lst.append(mat[row][col])
                diag_up = 1
                diag_down = 0
            # check if can go diagonally down
            elif row + 1 < n and col - 1 >= 0 and (not diag_up):
                while row < n and col > 0:
                    row += 1
                    col -= 1

                    if row < n and col < m:
                        # print('moving down:', mat[row][col])
                        lst.append(mat[row][col])
                    
                diag_up = 0
                diag_down = 1
            # check if left
            elif left:
                row += 1
                left = 0

                diag_up = 0
                diag_down = 0

                if row < n:
                    # print('moving row-1:', mat[row][col])
                    lst.append(mat[row][col])
            else:
                col += 1
                left = 1

                diag_up = 0
                diag_down = 0
                
                if col < m and row < n:
                    # print('moving left:', mat[row][col])
                    lst.append(mat[row][col])
        return lst
            

