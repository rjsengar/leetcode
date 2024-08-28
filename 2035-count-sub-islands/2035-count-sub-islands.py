class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n=len(grid1)
        m=len(grid1[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m or grid2[i][j]==0:
                return 
            grid2[i][j]=0
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j) 
        for i in range(n):
            for j in range(m):
                if grid1[i][j]!=grid2[i][j]:
                    if grid1[i][j]!=1:
                        dfs(i,j)
        c=0
        for i in range(n):
            for j in range(m):
                if grid2[i][j]==1:
                    c+=1
                    dfs(i,j)
        return c
        

        