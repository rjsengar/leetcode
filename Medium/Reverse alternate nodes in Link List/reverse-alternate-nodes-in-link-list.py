"""
  reverse alternate nodes and append at the end
  The input list will have at least one element
  Node is defined as
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

"""
class Solution:
    def rearrange(self, head):
        curr=head
        l=[]
        while(curr):
            l.append(curr.data)
            curr=curr.next
        l1=[]
        l2=[]
        for i in range(len(l)):
            if i%2==0:
                l1.append(l[i])
            else:
                l2.append(l[i])
        l2=l2[::-1]
        l1=l1+l2
        curr1=head
        i=0
        while(curr1):
            curr1.data=l1[i]
            i+=1
            curr1=curr1.next
        return head





#{ 
 # Driver Code Starts
# Node Class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains node object
class LinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Code execution starts here
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
            
        Solution().rearrange(llist.head)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
# } Driver Code Ends