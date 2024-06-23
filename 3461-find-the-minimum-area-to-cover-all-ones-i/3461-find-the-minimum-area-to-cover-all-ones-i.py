class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m1,m4=0,0
        m2,m3=100000,100000
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    m1=max(m1,i)
                    m2=min(m2,i)
                    m3=min(m3,j)
                    m4=max(m4,j)
        k=((m1-m2)+1)*((m4-m3)+1)
        return k
        