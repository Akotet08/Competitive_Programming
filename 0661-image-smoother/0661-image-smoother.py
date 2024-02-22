class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        new_lst = [[0] * n for _ in range(m)] 
        for row in range(m):
            for col in range(n):
                # get the eight surr cells
                # (0, 0) -> [(ca1), (ca1), (ca1), (ca1), (ca1) ... ]
                idxes = [(row-1, col),(row, col-1),(row -1, col-1), (row + 1, col), (row, col+1),(row+1, col+1), (row-1, col+1),(row+1, col-1)]
                eight_sum = 0
                counter = 0
                for idx in idxes:
                    r, c = idx
                    if r >=0 and c >= 0 and r < m and c < n:
                        eight_sum += img[r][c]
                        counter += 1
                new_lst [row][col] = (eight_sum + img[row][col]) // (counter + 1)
            
        return new_lst

                




        