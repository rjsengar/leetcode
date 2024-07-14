# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr=head
        head1=ListNode()
        head2=ListNode()
        curr1=head1
        curr2=head2
        while(curr):
            if curr.val<x:
                curr1.next=curr
                curr1=curr1.next
            else:
                curr2.next=curr
                curr2=curr2.next
            curr=curr.next
        curr2.next=None
        curr1.next=head2.next
        return head1.next


            