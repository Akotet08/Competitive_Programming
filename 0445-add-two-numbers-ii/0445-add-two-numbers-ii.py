# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        cur = l1
        while cur:
            num1.append(str(cur.val))
            cur = cur.next
        
        num2 = []
        cur = l2
        while cur:
            num2.append(str(cur.val))
            cur = cur.next
        
        s = str(int(''.join(num1)) + int(''.join(num2)))
        print(s)

        head = ListNode()
        cur = head
        count = 0
        for c in s:
            count += 1
            cur.val = int(c)
            cur.next = ListNode()
            if count == len(s):
                cur.next = None
            cur = cur.next
        
        return head



        