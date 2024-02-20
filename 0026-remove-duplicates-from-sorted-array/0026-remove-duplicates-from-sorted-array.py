class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        cur_num = nums[0]
        cur_pos = 1
        while i < len(nums):
            if nums[i] == cur_num:
                i+=1
                continue
            cur_num = nums[i]
            nums[cur_pos] = cur_num
            cur_pos += 1
        return cur_pos
            
                