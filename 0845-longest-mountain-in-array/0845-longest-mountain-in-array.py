class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        
        peak = 1
        length = 0
        while peak < len(arr)-1:
            left = peak
            while left > 0 and arr[left] > arr[left -1]:
                left -= 1
            
            right = peak
            while right < len(arr) -1 and arr[right] > arr[right + 1]:
                right += 1
            
            if (left - peak) == 0 or (right - peak) == 0:
                peak = right + 1
                continue
            
            peak = right + 1
            
            d = (right - left) + 1
            if d > length:
                length = d
        
        return length
            
                    

                    

        