# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur != None:
            val = cur.val
            node = cur.next
            while node != None and (val == node.val):
                node = node.next
            
            cur.next = node
            cur = cur.next
        
        return head

        