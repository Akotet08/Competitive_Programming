class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0

        avg = -float('inf')
        cur_avg = 0
        while i < len(nums):
            j = i + k

            if j > len(nums): break
            if i == 0:
                cur_avg = sum(nums[i:j])
            else:
                cur_avg -= nums[i-1]
                cur_avg += nums[i + k - 1]

                print(nums[i-1], nums[i + k - 1])
            
            if cur_avg > avg:
                avg = cur_avg
            i += 1
        
        return avg / k
            

