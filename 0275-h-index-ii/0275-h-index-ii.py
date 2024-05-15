class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        mx = n - 1 
        mn = 0
        while mn <= mx:
            mid = (mx + mn) // 2
            if n - mid == citations[mid]:
                return citations[mid]
            if (n - mid) > citations[mid]:
                mn = mid + 1
            else:
                mx = mid - 1

        return n - mn



        