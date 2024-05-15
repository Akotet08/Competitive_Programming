# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, lst):
        if root == None:
            return 

        self.helper(root.left, lst)
        lst.append(root.val)
        self.helper(root.right, lst)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.helper(root, lst)

        return lst
        