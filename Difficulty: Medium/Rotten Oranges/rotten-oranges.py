class Solution:
    #Function to find minimum time required to rot all oranges.
	def orangesRotting(self, grid):
	    n1=len(grid)
	    m1=len(grid[0])
	    q=[]
	    l=[]
	    
	    for i in range(len(grid)):
	        for j in range(m1):
	            if grid[i][j]==2:
	                
	                q.append([i,j])
	    c=0
	    arr1=[-1,1,0,0]
	    arr2=[0,0,1,-1]
	    while(q):
	        le=len(q)
	        t=0
	        while(le>0):
    	        i,j=q[0]
    	        n=q[0]
    	        q.remove(n)
    	       # grid[i][j]=2
    	        for f in range(4):
	                if i+arr1[f]<n1 and j+arr2[f]<m1 and i+arr1[f]>=0 and j+arr2[f]>=0:
	                    if grid[i+arr1[f]][j+arr2[f]]==1:
	                        grid[i+arr1[f]][j+arr2[f]]=2
	                        
	                        q.append([i+arr1[f],j+arr2[f]])
	                       
	                        t=1
                le-=1
	        if t:
	            c+=1
        # print(l)
        for i in grid:
            for j in i:
                if j==1:
                    return -1
	    return c
	    
	                    
	        
	    
		


#{ 
 # Driver Code Starts
from queue import Queue


T=int(input())
for i in range(T):
	n, m = map(int, input().split())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.orangesRotting(grid)
	print(ans)

# } Driver Code Ends