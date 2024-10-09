#User function Template for python3

'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Solution:
    def constructLinkedMatrix(self, mat):
        n=len(mat)
        i=0
        j=0
        p=[]
        l1=[]
        for i in range(n):
            p=[]
            for j in range(n):
                p.append(Node(mat[i][j]))
            l1.append(p)
        # print(l1)
        for i in range(n):
            for j in range(n):
                if j<n-1:
                    l1[i][j].right=l1[i][j+1]
                if i<n-1:
                    l1[i][j].down=l1[i+1][j]
            # l1.append(p)
        return l1[0][0]
        
        
        
        
        # while(l):
        #     a=l.pop(0)
        #     h=a[0]
        #     i=a[1]
        #     j=a[2]
        #     if i<n and j+1<n:
        #         h.next=Node(mat[i][j+1])
        #         l.append([h.next,i,j+1])
        #     if i+1<n and j<n:
        #         h.down=Node(mat[i+1][j])
        #         l.append([h.down,i+1,j])

        # return h1
        # for i in range(n):
        #     if i==0:
        #         h.next=Node(mat[0][i])
        #         h=h.next
        #         c=h
        #     for j in range(n):
        #         if i==0 and j==0:
        #             continue
        #         else:
        #             c.down=Node(mat[j][j])
        #             c=c.down
        # return h1
            
                
                
                
        


#{ 
 # Driver Code Starts
class Node():

    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None


def display(head):
    Dp = head
    while Dp:
        Rp = Dp
        while Rp:
            print(Rp.data, end=" ")
            if Rp.right:
                print(Rp.right.data, end=" ")
            else:
                print("null", end=" ")
            if Rp.down:
                print(Rp.down.data, end=" ")
            else:
                print("null", end=" ")
            Rp = Rp.right
        Dp = Dp.down


if __name__ == "__main__":
    for _ in range(int(input())):
        # First row input
        a = list(map(int, input().strip().split()))
        n = len(a)

        # Input the matrix
        mat = [a]
        for i in range(1, n):
            row = list(map(int, input().strip().split()))
            mat.append(row)

        # Create a Solution object and construct the linked matrix
        obj = Solution()
        head = obj.constructLinkedMatrix(mat)
        if head is None:
            print(-1)
            continue
        display(head)
        print()

# } Driver Code Ends