#User function Template for python3

class Solution:
	def findCoverage(self, matrix):
	    c=0
	    m=len(matrix)
	    n=len(matrix[0])
		for i in range(m):
		    for j in range(n):
		        if matrix[i][j]==0:
		            a1=i+1
		            a2=i-1
		            b1=j+1
		            b2=j-1
		            if a1<m and matrix[a1][j]==1:
		                c+=1
		            if a2>=0 and matrix[a2][j]==1:
		                c+=1
		            if b1<n and matrix[i][b1]==1:
		                c+=1
		            if b2>=0 and matrix[i][b2]==1:
		                c+=1
	    return c
		            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends