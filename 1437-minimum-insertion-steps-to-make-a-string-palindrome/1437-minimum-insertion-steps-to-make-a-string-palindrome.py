class Solution:
    def minInsertions(self, s: str) -> int:
        def solve(i,j,dp):
            if (i>=j) :
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==s[j]:
                dp[i][j]=solve(i+1,j-1,dp)
                return dp[i][j]
            else:
                dp[i][j]= min(solve(i+1,j,dp),solve(i,j-1,dp))+1
                return dp[i][j]
        dp=[[-1 for j in range(len(s))] for i in range(len(s))]
        print(dp)

        return solve(0,len(s)-1,dp)
        
        # i=0
        # j=len(s)-1
        # s=list(s)
        # s1=s[:]
        # while(i<j and i<len(s1) and j>=0):
        #     if s[i]==s[j]:
        #         i+=1
        #         j-=1
        #     else:
        #         s.insert(j,s[i])
        #         i+=1
        # return len(s)-len(s1)