# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        curr=head
        while(curr):
            arr.append(curr.val)
            curr=curr.next
        if k!=0 and len(arr)!=0:
            k=k%len(arr)
        m=[]
        l=len(arr)
        m=arr[l-k:]+arr[:l-k]
        curr=head
        i=0
        while(curr):
            curr.val=m[i]
            i+=1
            curr=curr.next
        return head