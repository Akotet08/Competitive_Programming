class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        new_lst = [[0] * n for _ in range(m)]

        for r in range(n):
            for c in range(m):
                new_lst[c][r] = matrix[r][c]
        
        return new_lst
        