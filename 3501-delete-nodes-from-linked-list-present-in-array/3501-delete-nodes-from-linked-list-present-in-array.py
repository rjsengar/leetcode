# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        d={}
        for i in nums:
            d[i]=1
        c1=h1=ListNode(-1)
        while(curr):
            if curr.val not in d:
                c1.next=ListNode(curr.val)
                c1=c1.next
            curr=curr.next
        return h1.next

        