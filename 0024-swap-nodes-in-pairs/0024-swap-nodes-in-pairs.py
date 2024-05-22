# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self, head):
        if not head:
            return None
        if not head.next:
            return head
        
        nxt = head.next
        nxt_head = self.helper(head.next.next)
        head.next.next = head
        head.next = nxt_head

        return nxt
        

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head)

       