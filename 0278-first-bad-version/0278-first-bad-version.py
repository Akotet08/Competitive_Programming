# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        r = n
        l = 1

        if n == 1:
            return 1

        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid - 1):
                    return mid
                r = mid - 1
            else:
                l = mid + 1


                
        