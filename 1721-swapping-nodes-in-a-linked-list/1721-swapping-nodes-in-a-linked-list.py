# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        size = 0

        while cur:
            size += 1
            cur = cur.next

        first = head
        second = head

        print(size)

        for _ in range(k-1):
            first = first.next
        
        for _ in range(size - k):
            second = second.next
        
        first.val, second.val = second.val, first.val

        return head
        