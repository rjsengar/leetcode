#User function Template for python3

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        l=[]
        if m==1:
            for i in matrix:
                l.append(i[0])
            return l
        if n==1:
            for i in matrix[0]:
                l.append(i)
            return l
        for i in matrix[0]:
            l.append(i)
        for i in range(1,n-1):
            l.append(matrix[i][m-1])
        for i in range(m-1,-1,-1):
            l.append(matrix[n-1][i])
        for i in range(n-2,0,-1):
            l.append(matrix[i][0])
        return l
            
            
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends