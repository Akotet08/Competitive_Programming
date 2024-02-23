from collections import Counter
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        zeros, ones = dic[0], dic[1]

        max_sum = 0
        cur_zeros = 0
        cur_ones = ones

        dic = {}

        for i in range(len(nums)):
            cur_sum = cur_zeros + cur_ones
            if cur_sum > max_sum:
                max_sum = cur_sum
            
            dic[i] = cur_sum

            if nums[i] == 0:
                cur_zeros += 1
            else:
                cur_ones -= 1
        
        dic[i+1] = cur_zeros + cur_ones
        if dic[i+1] > max_sum:
            max_sum = dic[i+1]

        lst = []
        for key in dic:
            if dic[key] == max_sum:
                lst.append(key)
        return lst


        
        