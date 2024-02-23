class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_sum = 0
        for row in range(n):
            for col in range(m):
                idxes = [(row-1, col), (row -1, col-1),
                         (row + 1, col), (row+1, col+1),
                         (row-1, col+1),(row+1, col-1), (row, col)]
                cur_sum = 0
                for idx in idxes:
                    r, c = idx
                    if r >=0 and c >=0 and r < n and c < m:
                        cur_sum += grid[r][c]
                    else:
                        cur_sum = 0
                        break
                if cur_sum > max_sum:
                    max_sum = cur_sum

        return max_sum



        