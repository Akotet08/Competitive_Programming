class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        lst = set()
        for i in range(len(nums)):
            for m in range(i+1, len(nums)):
                j = i + 1
                k = len(nums) - 1

                while j < k:
                    s = nums[j] + nums[k] + nums[i] + nums[m]
                    if s > target:
                        k -= 1
                    elif s < target:
                        j += 1
                    else:
                        if j != i and k!=i and j != m and k != m:
                            if i < j:
                                lst.add(tuple(sorted((nums[i], nums[m], nums[j], nums[k]))))
                        j += 1
                        k -= 1
        
        return list(lst)
        