class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        parts=[]
        cur=head
        l=0 
        while cur:
            l+=1
            cur=cur.next
        
        n,r=divmod(l,k)
        
        cur=head
        while cur:
            dummy=ListNode()
            cur2=dummy
            for _ in range(n):
                cur2.next=cur
                cur=cur.next
                cur2=cur2.next
            if r:
                cur2.next=cur
                cur=cur.next
                cur2=cur2.next
                r-=1
            
            cur2.next=None

            parts.append(dummy.next)

        while len(parts)<k:
            parts.append(None)

        return parts