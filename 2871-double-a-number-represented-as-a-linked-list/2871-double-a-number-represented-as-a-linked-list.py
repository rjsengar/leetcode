# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        s=0
        while(curr):
            s=s*10+curr.val
            curr=curr.next
        s*=2
        if s==0:
            h=ListNode(0)
            return h
            
        l=[]
        while(s>0):
            d=s%10
            l.append(str(d))
            s=s//10
        l=l[::-1]
        c=h=ListNode(-1)
        for i in l:
            c.next=ListNode(int(i))
            c=c.next
        return h.next
            

        