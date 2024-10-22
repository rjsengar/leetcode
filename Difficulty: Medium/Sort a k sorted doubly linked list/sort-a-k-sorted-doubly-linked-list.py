#User function Template for python3
'''
class DLLNode:
    def __init__(self,val) -> None:
        self.data = val
        self.prev = None
        self.next = None
'''
from queue import PriorityQueue 
class Solution:
    def sortAKSortedDLL(self, head, k):
        curr=head
        l=[]
        l2=[]
        q=PriorityQueue()
        while(curr):
            l.append(curr.data)
            curr=curr.next
        l1=l[:k+1]
        for i in l1:
            q.put(i)
        for i in range(k+1,len(l)):
            l2.append(q.get())
            q.put(l[i])
        while(q.qsize()):
            l2.append(q.get())
        curr=head
        for i in l2:
            curr.data=i
            curr=curr.next
    
        return head
            
        

        return head
#{ 
 # Driver Code Starts
import heapq


# A node of the doubly linked list
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


# Function to insert a node at the end of the doubly linked list
def push(tail, new_data):
    new_node = DLLNode(new_data)
    new_node.next = None
    new_node.prev = tail

    if tail is not None:
        tail.next = new_node

    return new_node


# Function to print nodes in a given doubly linked list
def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


# Driver code
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        arr = list(map(int, input().split()))  # Read the input array
        k = int(input())  # Read the value of k

        head = DLLNode(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail = push(tail, arr[i])

        solution = Solution()
        sorted_head = solution.sortAKSortedDLL(head, k)
        printList(sorted_head)

# } Driver Code Ends