# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr=head
        c=0
        while(curr):
            c+=1
            curr=curr.next
        i=0
        curr=head
        m=c//k
        i=0
        l=[0]*k
        j=0
        while(c):
            l[j]+=1
            j+=1
            c-=1
            j=j%k
        print(l)
        l1=[]
        i=0
        while(curr):
            c=0
            c1=h1=ListNode(-1)
            while(c<l[i]):
                c1.next=ListNode(curr.val)
                curr=curr.next
                c1=c1.next
                c+=1
            l1.append(h1.next)
            i+=1
        while(len(l1)!=k):
            l1.append(None)

        return l1


            
        
        