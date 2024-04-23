"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # first loop to copy without random
        if head == None:
            return None
        new_head = Node(head.val)
        new_cur = new_head
        cur = head
        while cur != None:
            new_cur.val = cur.val
            if cur.next == None:
                new_cur.next = None
            else:
                new_cur.next = Node(cur.next.val)
            
            cur.cp = new_cur
            cur = cur.next
            new_cur = new_cur.next
        
        cur = head
        while cur != None:
            if cur.random == None:
                cur.cp.random = None
            else:
                cur.cp.random = cur.random.cp
            cur = cur.next
        
        return new_head
            
            
            