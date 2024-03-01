class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        dic = {}
        for ele in nums:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        
        lst = sorted(list(dic.keys()))
        ops = 0
        for i in range(len(lst)):
            ops += i * dic[lst[i]]
        return ops
