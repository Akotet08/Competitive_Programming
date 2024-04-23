# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0

        cur = head
        while cur != None:
            size += 1
            cur = cur.next
        
        mid = (size) // 2

        cur = head
        for _ in range(mid):
            cur = cur.next
        
        return cur
