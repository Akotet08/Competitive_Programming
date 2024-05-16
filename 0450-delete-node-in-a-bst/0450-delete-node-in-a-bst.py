# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, parent, key):
        if not root:
            return None
        
        if key < root.val:
            l = self.helper(root.left, root, key)
            root.left = l
            return root

        if key > root.val:
            r = self.helper(root.right, root, key)
            root.right = r
            return root
        
        else:
            # find successor node to replace
            if not root.right and not root.left:
                return None
            if not root.right:
                if not parent and not root.left:
                    return None
                return root.left
            else:
                successor = root.right
                p = root
                while successor.left:
                    p = successor
                    successor = successor.left
                
                if p == root:
                    p.right = successor.right
                else:
                    p.left = successor.right
                root.val = successor.val

                return root
            
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.helper(root, None, key)
        