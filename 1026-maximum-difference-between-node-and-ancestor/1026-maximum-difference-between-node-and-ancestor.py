# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return (0, (-1, -1))
        
        diff, (mn, mx) = self.helper(root.left)
        diff2, (mn2, mx2) = self.helper(root.right)

        if mn == -1: mn = root.val
        if mx == -1: mx = root.val
        if mn2 == -1: mn2 = root.val
        if mx2 == -1: mx2 = root.val

        mn = min(mn, mn2)
        mx = max(mx, mx2)
        
        c = max(abs(root.val - mn), abs(root.val - mx))

        if root.val < mn:
            mn = root.val
        elif root.val > mx:
            mx = root.val
        
        d = max(diff, diff2, c)
        
        return (d, (mn, mx))
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        r = self.helper(root)
        return r[0]

        

        
