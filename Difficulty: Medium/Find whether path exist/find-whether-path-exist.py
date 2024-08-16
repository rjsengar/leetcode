
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
	    n=len(grid)
	    l=[]
	    p=[]
	    
	    
		def tree(i,j):
		    if i<0 or i>=n or j<0 or j>=n or grid[i][j]==0:
		        return 0
		    if (i>=0 and i<n and j>=0 and j<n) and  grid[i][j]==2:
		        l.append(1)
		        return 1
		    grid[i][j]=0
		    return tree(i+1,j) or tree(i-1,j) or tree(i,j+1) or tree(i,j-1)
		for i in range(len(grid)):
		    for j in range(len(grid)):
		        if grid[i][j]==1:
		            p=[i,j]
		            break
		    if p:
		        break
		if p:
		    tree(p[0],p[1])
		    if l:
		        return 1
		    return 0
		return 0
		


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.is_Possible(grid)
	if(ans):
		print("1")
	else:
		print("0")

# } Driver Code Ends