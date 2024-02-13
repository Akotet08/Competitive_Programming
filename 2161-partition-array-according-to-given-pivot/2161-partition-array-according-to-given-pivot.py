class Solution:        
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [0] * len(nums)

        i = 0
        for ele in nums:
            if ele < pivot:
                res[i] = ele
                i += 1

        for ele in nums:
            if ele == pivot:
                res[i] = ele
                i += 1
        
        for ele in nums:
            if ele > pivot:
                res[i] = ele
                i += 1
        
        return res
                


        
        