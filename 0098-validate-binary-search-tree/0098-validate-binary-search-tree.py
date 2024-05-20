# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return (True, [])
        
        l, chrn_l = self.helper(root.left)
        if l == False: return (False, [])
        for ele in chrn_l:
            if ele >= root.val:
                return (False, [])
        
        r, chrn_r = self.helper(root.right)
        if r == False: return (False, [])
        for ele in chrn_r:
            if ele <= root.val:
                return (False, [])

        chrn = chrn_l + chrn_r
        chrn.append(root.val)

        return (True, chrn)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val, _  = self.helper(root)
        return val
        