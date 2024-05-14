class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checker(piles, k, h):
            time = 0
            i = 0
            while i < len(piles):
                if piles[i] <= k:
                    time += 1
                else:
                    time += ceil(piles[i] / k)
                i += 1
            
            return time <= h

        mx = max(piles) * len(piles)
        mn = 1

        while mn < mx:
            mid = (mn + mx) // 2
            if checker(piles, mid, h):
                mx = mid
            else:
                mn = mid + 1

        return mn 
        