class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        l = 0
        r = (len(matrix) * len(matrix[0]))- 1

        while l <= r:
            mid = (l + r)//2
        
            x, y = mid // n, mid % n

            if matrix[x][y] == target:
                return True

            if matrix[x][y] > target:
                r = mid - 1
            else:
                l = mid + 1
                 
        return False
            