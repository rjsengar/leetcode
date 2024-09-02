class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dp=[]
        for i in range(n):
            l1=[]
            for j in range(n):
                if i==0:
                    l1.append(grid[i][j])
                else:
                    l1.append(0)
            dp.append(l1)
        for i in range(1,n):
            for j in range(n):
                m=float('inf')
                for k in range(n):
                    if k!=j:
                        m=min(m,dp[i-1][k]+grid[i][j])
                dp[i][j]=m
        m1=float('inf')
        for i in range(n):
            m1=min(m1,dp[n-1][i])
        return m1
