#User function Template for python3

class Solution:
    def maximumPath(self, N, matrix):
        dp=[]
        for i in range(N):
            l1=[]
            for j in range(N):
                if i==0:
                    l1.append(matrix[i][j])
                else:
                    l1.append(0)
            dp.append(l1)
        for i in range(1,N):
            for j in range(N):
                a=matrix[i][j]+dp[i-1][j]
                if j-1>=0:
                    b=matrix[i][j]+dp[i-1][j-1]
                else:
                    b=-float('inf')
                if j+1<N:
                    c=matrix[i][j]+dp[i-1][j+1]
                else:
                    c=-float('inf')
                dp[i][j]=max(a,b,c)
        m=0
        for i in range(N):
            m=max(m,dp[N-1][i])
        return m
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends