class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        rmax = 0
        lmax = 0
        area = 0
        while i < j:
            if height[i] > lmax: lmax = height[i]
            if height[j] > rmax: rmax = height[j]
            if(rmax > lmax):
                area += lmax - height[i]
                i += 1
            else:
                area += rmax - height[j]
                j -= 1
        return area
            
            

                
