class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        mx_area = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            a = (j - i) * min(height[i], height[j])
            if a > mx_area:
                mx_area = a 
            
        return mx_area