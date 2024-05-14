class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = {s:i for i,  (s, e) in enumerate(intervals)}
        
        s_sorted = sorted(starts.keys())
        res = []
        for s, e in intervals:
            l = 0
            r = len(s_sorted) -1 

            while l < r:
                mid = (l + r) // 2

                if s_sorted[mid] >= e:
                    r = mid
                else:
                    l = mid + 1
            
            if(s_sorted[l] >= e): res.append(starts[s_sorted[l]])
            else: res.append(-1)

        return res


