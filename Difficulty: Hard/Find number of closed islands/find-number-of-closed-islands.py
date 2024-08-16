#User function Template for python3

class Solution:
	def closedIslands(self, grid, N, M):
	    def tree(i,j):
	        if i<0 or i>=N or j<0 or j>=M or grid[i][j]==0:
	            return
	        grid[i][j]=0
	        tree(i+1,j)
	        tree(i-1,j)
	        tree(i,j-1)
	        tree(i,j+1)
		for i in range(N):
		    if grid[i][0]==1:
		        tree(i,0)
		    if grid[i][M-1]==1:
		        tree(i,M-1)
		for j in range(M):
		    if grid[0][j]==1:
		        tree(0,j)
		    if grid[N-1][j]==1:
		        tree(N-1,j)
		c=0
		for i in range(N):
		    for j in range(M):
		        if grid[i][j]==1:
		            tree(i,j)
		            c+=1
# 		print(grid)
		return c
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N, M = map(int,input().split())
        matrix = []
        for i in range(N):
            nums = list(map(int,input().split()))
            matrix.append(nums)
        obj = Solution()
        print(obj.closedIslands(matrix, N, M))
# } Driver Code Ends