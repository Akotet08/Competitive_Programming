# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        cur = head
        prev = dummy
        while cur != None:
            val = cur.val
            node = cur.next
            if node != None and (val == node.val):
                while node != None and (val == node.val): 
                    node = node.next
                
                prev.next = node
                cur = node
            else:
                prev = cur
                cur = cur.next
        
        return dummy.next
