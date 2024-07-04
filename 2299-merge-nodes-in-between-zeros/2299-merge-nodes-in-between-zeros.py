# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        c1=0
        c=h=ListNode(-1)
        while(curr):
            c1=0
            while(curr.val):
                c1+=curr.val
                curr=curr.next
            if curr:
                curr=curr.next
            if c1:
                h.next=ListNode(c1)
                h=h.next
        return c.next


        