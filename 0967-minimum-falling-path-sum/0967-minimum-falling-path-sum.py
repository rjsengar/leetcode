class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        dp=[]
        m1=float('inf')
        for i in range(n):
            l1=[]
            for j in range(n):
                if i==0:
                    l1.append(matrix[i][j])
                else:
                    l1.append(0)
            dp.append(l1)
        # print(dp)
        for i in range(1,n):
            for j in range(n):
                a=matrix[i][j]+dp[i-1][j]
                if j-1>=0:
                    b=matrix[i][j]+dp[i-1][j-1]
                else:
                    b=float('inf')
                if j+1<n:
                    c=matrix[i][j]+dp[i-1][j+1]
                else:
                    c=float('inf')
                dp[i][j]=min(a,b,c)
        # print(dp)
        for i in range(n):
            m1=min(m1,dp[n-1][i])
        return m1
        # m=10000000
        # def solve(i,j,matrix):
        #     if j<0 or j>=n:
        #         return 100000000
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     if i==0:
        #         return matrix[i][j]
        #     a=matrix[i][j]+solve(i-1,j,matrix)
        #     b=matrix[i][j]+solve(i-1,j-1,matrix)
        #     c=matrix[i][j]+solve(i-1,j+1,matrix)
        #     dp[i][j]=min(a,b,c)
        #     return dp[i][j]
        # m=10000000
        # for j in range(n):
        #     m=min(m,solve(n-1,j,matrix))
        # return m
        
        