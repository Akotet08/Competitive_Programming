# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        cur = node.next
        while cur != None:
            prev.val = cur.val

            if cur.next:
                prev = cur
            else:
                prev.next = None
            cur = cur.next
        prev = None
        
