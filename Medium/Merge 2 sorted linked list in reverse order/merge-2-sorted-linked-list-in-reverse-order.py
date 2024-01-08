#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Solution:
    def mergeResult(self, h1, h2):
        def reverse_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        c=h=Node(-1)
        # l1=[]
        # l2=[]
        # while(h1):
        #     l1.append(h1.data)
        #     h1=h1.next
        # while(h2):
        #     l2.append(h2.data)
        #     h2=h2.next
        # l1=l1[::-1]
        # l2=l2[::-1]
        # i=0
        # j=0
        while(h1 and h2):
            if h1.data>h2.data:
                c.next=Node(h2.data)
                h2=h2.next
            else:
                c.next=Node(h1.data)
                h1=h1.next
            c=c.next
        if h1:
            while(h1):
                c.next=Node(h1.data)
                h1=h1.next
                c=c.next
        if h2:
            while(h2):
                c.next=Node(h2.data)
                h2=h2.next
                c=c.next
        m=reverse_list(h.next)
        return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1,n2=[int(x) for x in input().split()]
        
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        arr2=[int(x) for x in input().split()]
        ll2=Llist()
        tail=None
        for nodeData in arr2:
            tail=ll2.insert(nodeData,tail)
        
        
        ob = Solution()
        resHead=ob.mergeResult(ll1.head,ll2.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends