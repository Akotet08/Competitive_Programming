class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = [x for (x,y) in points]
        xs.sort()
        
        dif = 0
        for i in range(len(xs) - 1):
            d = xs[i+1] - xs[i]
            if d > dif:
                dif = d
        return dif
        