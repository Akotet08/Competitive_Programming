# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_node = head
        slow_node = head
        
        while fast_node != None and slow_node != None:
            if fast_node.next != None:
                if fast_node.next.next != None:
                    slow_node = slow_node.next
                    fast_node = fast_node.next.next
                else:
                    return None
            else:
                return None
            
            if slow_node == fast_node:
                node = head
                while node != slow_node:
                    slow_node = slow_node.next
                    node = node.next 
                return slow_node
        return None
                    
            