class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        output = [-1] * len(nums2)
        
        mapp = {ele: idx for idx, ele in enumerate(nums2)}

        for idx in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[idx]:
                p = stack.pop()
                output[p] = nums2[idx]
            
            stack.append(idx)
        
        out = [-1] * len(nums1)
        for idx in range((len(nums1))):
            if nums1[idx] in mapp:
                out[idx] = output[mapp[nums1[idx]]]

        return out



