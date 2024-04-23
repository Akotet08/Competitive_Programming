# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find half
        fast_node = head
        slow_node = head
        
        while fast_node != None:
            if fast_node.next != None:
                fast_node = fast_node.next.next
                slow_node = slow_node.next
            else:
                break
        # reverse the send half
        lst = self.reverse(slow_node)
        node = head
        
        while lst != None:
            if lst.val != node.val:
                return False
            lst = lst.next
            node = node.next
        return True
            
    
    def reverse(self, head):
        pre_node = None
        cur_node = head
        while cur_node != None:
            temp = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = temp
        return pre_node