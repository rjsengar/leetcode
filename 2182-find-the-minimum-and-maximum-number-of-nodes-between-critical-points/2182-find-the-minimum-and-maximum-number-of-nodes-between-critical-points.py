# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        l=[]
        l1=[]
        curr=head
        while(curr):
            l.append(curr.val)
            curr=curr.next
        for i in range(1,len(l)-1):
            if l[i]>l[i-1] and l[i]>l[i+1]:
                l1.append(i)
            elif l[i]<l[i-1] and l[i]<l[i+1]:
                l1.append(i)
        if len(l1)<=1:
            return [-1,-1]
        else:
            l1.sort()
            ma=0
            m=1000000
            for i in range(len(l1)-1):
                m=min(m,l1[i+1]-l1[i])
            ma=l1[-1]-l1[0]
            return [m,ma]
        