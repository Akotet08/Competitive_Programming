class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        def check(houses, heaters, k):
            hs_pointer = 0
            htr_pointer = 0

            while hs_pointer < len(houses):
                while htr_pointer < len(heaters) and abs(heaters[htr_pointer] - houses[hs_pointer]) > k:
                    htr_pointer += 1

                if htr_pointer >= len(heaters):
                    return False

                hs_pointer += 1
            
            return True

        houses.sort()
        heaters.sort()
                 
        l = 0
        r = max(heaters[-1], houses[-1])

        while l < r:

            mid = (l + r) // 2

            if check(houses, heaters, mid):
                r = mid
            else:
                l = mid + 1
        
        return l
