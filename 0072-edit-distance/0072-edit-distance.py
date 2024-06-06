def solve(s1,s2,m,n,dp):
    if m==0:
        return n
    if n==0:
        return m
    if dp[m][n]!=-1:
        return dp[m][n]
    if s1[m-1]==s2[n-1]:
        dp[m][n]=solve(s1,s2,m-1,n-1,dp)
        return dp[m][n]
    dp[m][n]=1+min(solve(s1,s2,m-1,n-1,dp),solve(s1,s2,m-1,n,dp),solve(s1,s2,m,n-1,dp))
    return dp[m][n]
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp=[]
        for i in range(m+1):
            l=[]
            for j in range(n+1):
                l.append(-1)
            dp.append(l)
        s=solve(word1,word2,m,n,dp)
        return s