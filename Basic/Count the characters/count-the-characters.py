#User function Template for python3

class Solution:
    def getCount (self,S, N):
        d={}
        for i in range(len(S)):
            if S[i] in d and S[i-1]!=S[i]:
                d[S[i]]+=1
            elif S[i] not in d:
                d[S[i]]=1
        c=0
        for i in d:
            if d[i]==N:
                c+=1
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s, n = input().split()
    s = str(s)
    n = int(n)
    ob = Solution()
    print (ob.getCount (s, n))

# Contributed By: Pranay Bansal

# } Driver Code Ends