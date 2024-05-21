# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append([root, 1])

        width = 1
        
        while q:
            
            width = max(width, q[-1][1] - q[0][1] + 1)

            for i in range(len(q)):
                node, num = q.popleft()
                
                if node.left: q.append([node.left, 2 * num])
                if node.right: q.append([node.right, (2 * num) + 1])
                    
        return width

