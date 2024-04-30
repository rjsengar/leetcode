#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        curr1=first
        curr2=second
        arr1=[]
        arr2=[]
        while(curr1):
            arr1.append(curr1.data)
            curr1=curr1.next
        while(curr2):
            arr2.append(curr2.data)
            curr2=curr2.next
        s1=0
        s2=0
        l=[]
        for i in arr1:
            s1=s1*10+i
        for i in arr2:
            s2=s2*10+i
        s1=s1+s2
        while(s1!=0):
            d=s1%10
            l.append(d)
            s1=s1//10
        l=l[::-1]
        head=Node(10000)
        curr=head
        i=0
        while(i<len(l)):
            curr.next=Node(l[i])
            curr=curr.next
            i+=1
        if head.next==None:
            return Node(0)
        return head.next
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)
        
        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
# } Driver Code Ends