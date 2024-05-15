# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, lst):
        if not root:
            return 
        
        self.helper(root.left, lst)
        self.helper(root.right, lst)
        lst.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.helper(root, lst)

        return lst
        