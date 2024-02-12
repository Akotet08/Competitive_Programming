class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        lo = -1
        hi = num // 3

        while lo < hi:
            mid = (lo + hi) // 2 
            sm = 3 * (mid + 1)
           
            if sm == num:
                return [mid, mid + 1, mid + 2]
            elif sm > num:
                hi = mid - 1 
            else:
                lo = mid + 1

            
    

        