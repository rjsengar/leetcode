class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        c=0
        m=len(grid)
        n=len(grid[0])
        i=0
        j=m-1
        while(i<j):
            for k in range(n):
                if grid[i][k]^grid[j][k]:
                    c+=1
            i+=1
            j-=1
        i=0
        j=n-1
        c1=0
        while(i<j):
            for k in range(m):
                if grid[k][i]^grid[k][j]:
                    c1+=1
            i+=1
            j-=1
        return min(c1,c)