# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        node = dummy = ListNode(0, None)
        nodeOne = l1
        nodeTwo = l2
        
        while nodeOne != None and nodeTwo != None:
            s = nodeOne.val + nodeTwo.val + carry
            carry = s // 10
            t = s % 10
                    
            temp = ListNode(t, None)
            node.next = temp
            
            nodeOne = nodeOne.next
            nodeTwo = nodeTwo.next
            node = node.next
            
        while nodeOne != None:
            s = nodeOne.val + carry
            carry = s // 10
            t = s % 10
                    
            temp = ListNode(t, None)
            node.next = temp
            
            nodeOne = nodeOne.next
            node = node.next
            
        while nodeTwo != None:
            s = nodeTwo.val + carry
            carry = s // 10
            t = s % 10
                    
            temp = ListNode(t, None)
            node.next = temp
            
            nodeTwo = nodeTwo.next
            node = node.next
            
        if carry != 0:
            node.next = ListNode(carry, None)
        return dummy.next
        
        
            
        
        
        