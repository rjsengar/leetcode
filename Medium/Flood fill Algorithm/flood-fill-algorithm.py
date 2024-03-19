class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    n=len(image)
	    m=len(image[0])
	    a=image[sr][sc]
		def dfs(i,j):
		    if i<0 or j<0 or i>=n or j>=m or image[i][j]!=a or image[i][j]==newColor:
		        return
		    image[i][j]=newColor
		    dfs(i+1,j)
		    dfs(i-1,j)
		    dfs(i,j+1)
		    dfs(i,j-1)
		dfs(sr,sc)
		return image
		    



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)


T=int(input())
for i in range(T):
	n, m = input().split()
	n = int(n)
	m = int(m)
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))
	sr, sc, newColor = input().split()
	sr = int(sr); sc = int(sc); newColor = int(newColor);
	obj = Solution()
	ans = obj.floodFill(image, sr, sc, newColor)
	for _ in ans:
		for __ in _:
			print(__, end = " ")
		print()
# } Driver Code Ends