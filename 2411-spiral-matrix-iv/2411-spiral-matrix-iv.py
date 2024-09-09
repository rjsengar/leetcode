# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        l=[]
        for i in range(m):
            l1=[]
            for j in range(n):
                l1.append(-1)
            l.append(l1)
        left=0
        right=n-1
        top=0
        bottom=m-1
        curr=head
        while(1):
            for i in range(left,right+1):
                if curr:
                    l[top][i]=curr.val
                    curr=curr.next
            top+=1
            # print(top,i,'l')
            for i in range(top,bottom+1):
                if curr:
                    l[i][right]=curr.val
                    curr=curr.next
            right-=1
            for i in range(right,left-1,-1):
                if curr:
                    l[bottom][i]=curr.val
                    curr=curr.next
            bottom -=1
            print(bottom,left)
            for i in range(bottom,top-1,-1):
                if curr:
                    l[i][left]=curr.val
                    curr=curr.next
            left+=1
            if curr==None:
                break
            
        return l


        
        