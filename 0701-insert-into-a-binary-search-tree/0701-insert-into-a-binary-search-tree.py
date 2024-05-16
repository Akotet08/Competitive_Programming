# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val = val)
        
        if val < root.val:
            left_tree = self.insertIntoBST(root.left, val)
            root.left = left_tree
        
        else:
            right_tree = self.insertIntoBST(root.right, val)
            root.right = right_tree
        
        return root
        