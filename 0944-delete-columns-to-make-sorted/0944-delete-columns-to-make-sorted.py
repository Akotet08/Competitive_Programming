class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        count = 0
        for c in range(cols):
            prev = ''
            for r in range(rows):
                if prev == '':
                    prev = strs[r][c]
                    continue
                if strs[r][c] < prev:
                    count += 1
                    break
                else:
                    prev = strs[r][c]
        return count

                



        