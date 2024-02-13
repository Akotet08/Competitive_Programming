class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        evenpos = 0
        oddpos = 1

        for ele in nums:
            if ele < 0:
                res[oddpos] = ele
                oddpos += 2
            elif ele > 0:
                res[evenpos] = ele
                evenpos += 2
        
        return res
