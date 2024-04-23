# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_node = head
        slow_node = head
        
        while fast_node != None and slow_node != None:
            if fast_node.next != None:
                if fast_node.next.next != None:
                    slow_node = slow_node.next
                    fast_node = fast_node.next.next
                else:
                    return False
            else:
                return False
            
            if fast_node == slow_node:
                return True
            
        return False
        