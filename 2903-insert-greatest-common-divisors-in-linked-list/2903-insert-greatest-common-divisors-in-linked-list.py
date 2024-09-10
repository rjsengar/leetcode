# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def gcd(a,b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=h=ListNode(head.val)
        k=0
        curr=head
        d=0
        while(curr.next):
            a=gcd(curr.val,curr.next.val)
            c.next=ListNode(a)
            c=c.next
            c.next=ListNode(curr.next.val)
            c=c.next
            curr=curr.next
        return h
        