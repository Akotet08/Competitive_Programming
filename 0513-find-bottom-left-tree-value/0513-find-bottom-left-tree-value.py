# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        # check if last row
        if not root:
            return (None, 0)
        
        l_node, l_d = self.helper(root.left)
        r_node, r_d = self.helper(root.right)
        
        if l_node == None:
            l_node = root.val
        if r_node == None:
            r_node == root.val
        
        if l_d < r_d:
            return (r_node, r_d + 1)
        return (l_node, l_d + 1)
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        node, _ = self.helper(root)

        return node
        