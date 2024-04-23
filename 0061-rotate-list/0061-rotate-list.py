# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        n = 0
        cur = head
        while cur != None:
            n += 1
            cur = cur.next
        
        f = n - (k % n)
        
        print(f)
        
        if f == n:
            return head
        
        cur = head
        for i in range(f - 1):
            cur = cur.next
        
        temp = head
        head = cur.next
        cur.next = None
        
        new_cur = head
        while new_cur.next != None:
            new_cur = new_cur.next
        
        new_cur.next = temp
        
        return head
        
            
        