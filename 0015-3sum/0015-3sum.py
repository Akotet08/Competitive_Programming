class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        lst = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[j] + nums[k] + nums[i]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    if j != i and k!=i:
                        if i < j:
                            lst.add((nums[i], nums[j], nums[k]))
                        elif i > j and i < k:
                            lst.add((nums[j], nums[i], nums[k]))     
                        else:
                            lst.add((nums[j], nums[k], nums[i]))     
                    j += 1
                    k -= 1
        
        return list(lst)


            


        


        