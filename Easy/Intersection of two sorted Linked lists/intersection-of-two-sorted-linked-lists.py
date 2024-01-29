#User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

class Solution:
    def findIntersection(self,head1,head2):
        curr1=head1
        curr2=head2
        arr1=[]
        arr2=[]
        d1={}
        d2={}
        l=[]
        while(curr1):
            arr1.append(curr1.data)
            if curr1.data in d1:
                d1[curr1.data]+=1
            else:
                d1[curr1.data]=1
            curr1=curr1.next
        while(curr2):
            arr2.append(curr2.data)
            if curr2.data in d2:
                d2[curr2.data]+=1
            else:
                d2[curr2.data]=1
            curr2=curr2.next
        for i in arr1:
            if d1[i]>0 and i in d2:
                if d2[i]>0:
                    l.append(i)
                    d1[i]-=1
                    d2[i]-=1
        head=Node(10000)
        curr=head
        i=0
        while(i<len(l)):
            curr.next=Node(l[i])
            curr=curr.next
            i+=1
        return head.next




#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        n1,n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        ob = Solution()
        result = ob.findIntersection(ll1.head,ll2.head)
        printList(result)
        print()

# } Driver Code Ends