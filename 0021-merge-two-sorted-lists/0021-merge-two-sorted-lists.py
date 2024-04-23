# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        
        newhead = None
        newNode = None
                
        while node1 != None and node2 != None:
            temp = 0
            if node1.val <= node2.val:
                temp = node1.val
                node1 = node1.next
            else:
                temp = node2.val
                node2 = node2.next
                
            if newhead == None:
                newhead = ListNode(temp, None)
                newNode = newhead
            else:
                t = ListNode(temp, None)
                newNode.next = t
                newNode = newNode.next
                
        while node1 != None:
            t = ListNode(node1.val, None)
            
            if newhead == None:
                newhead = ListNode(node1.val, None)
                newNode = newhead
            else:
                newNode.next = t
                newNode = newNode.next
                
            node1 = node1.next
        while node2 != None:
            t = ListNode(node2.val, None)
            
            if newhead == None:
                newhead = ListNode(node2.val, None)
                newNode = newhead
            else:  
                newNode.next = t
                newNode = newNode.next
            node2 = node2.next
        return newhead