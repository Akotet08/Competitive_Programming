# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(head.val, head)
        
        left_node = head
        for _ in range(left -  1):
            left_node = left_node.next
        
        right_node = left_node
        cur = left_node
        for _ in range(right - left):
            right_node = cur.next
            right_node.prev = cur
            cur = cur.next

            # print(right_node.val, right_node.prev.val)
        
        for _ in range((right - left)//2 + (right - left)%2):
            left_node.val, right_node.val = right_node.val, left_node.val
            left_node = left_node.next
            right_node = right_node.prev 

            

        return head