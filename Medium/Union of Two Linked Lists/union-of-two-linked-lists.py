#User function Template for python3

class Solution:
    def union(self, head1,head2):
        curr1=head1
        curr2=head2
        l=[]
        l1=[]
        l2=[]
        while(curr1):
            l1.append(curr1.data)
            curr1=curr1.next
        while(curr2):
            l2.append(curr2.data)
            curr2=curr2.next
        l=l1
        for i in l2:
            l.append(i)
        l=list(set(l))
        l.sort()
        head=Node(0)
        curr=head
        for i in l:
            curr.next=Node(i)
            curr=curr.next
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
    for _ in range(int(input())):
        
        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        ob = Solution()
        printList(ob.union(ll1.head,ll2.head))
        print()

# } Driver Code Ends