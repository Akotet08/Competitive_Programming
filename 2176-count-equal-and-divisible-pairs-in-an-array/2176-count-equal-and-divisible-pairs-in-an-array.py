class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = {}

        count = 0
        for idx, ele in enumerate(nums):
            if ele in dic:
                for i in dic[ele]:
                    if (idx * i) % k == 0:
                        count += 1
                dic[ele].append(idx)
            else:
                dic[ele] = [idx]
        
        return count
