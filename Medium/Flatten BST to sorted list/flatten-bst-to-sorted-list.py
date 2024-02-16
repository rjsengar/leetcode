#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
# def tree(root,l):
#     if root==None:
#         return
#     tree(root.left,l)
#     l.append(root.data)
#     tree(root.right,l)
    
    
class Solution:
    def flattenBST(self, root):
        q=[root]
        l=[]
        while(len(q)):
            l1=len(q)
            while(l1>0):
                n=q[0]
                q.remove(n)
                l.append(n.data)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                l1-=1
        l.sort()
        # print(l)
        c=n=Node(l[0])
        for i in range(1,len(l)):
            n.right=Node(l[i])
            n=n.right
        return c
    
        






#{ 
 # Driver Code Starts

#Initial Template for Python 3

from queue import Queue

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def newNode(key):
    node = Node(key)
    return node

def buildTree(s):
    if len(s) == 0 or s[0] == 'N':
        return None

    ip = s.split()
    root = newNode(int(ip[0]))
    q = Queue()
    q.put(root)

    i = 1
    while not q.empty() and i < len(ip):
        currNode = q.get()

        currVal = ip[i]
        if currVal != "N":
            currNode.left = newNode(int(currVal))
            q.put(currNode.left)

        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]
        if currVal != "N":
            currNode.right = newNode(int(currVal))
            q.put(currNode.right)

        i += 1

    return root


def printList(head):
    # if head==None:
    #     return
    # print(head.data, end=" ")
    # printList(head.left)
    # printList(head.right)
    while head:
        if head.left:
            print(-1,end=" ")
        print(head.data, end=" ")
        head = head.right
        
    print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        ans = ob.flattenBST(root)
        printList(ans)
        # print()

# } Driver Code Ends