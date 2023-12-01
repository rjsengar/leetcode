#User function Template for python3

class Solution:
    def nCr(self, n, r):
        if r>n:
            return 0
        n1=1
        r1=1
        k=1
        for i in range(1,n+1):
            n1=n1*i
        for j in range(1,r+1):
            r1=r1*j
        for i in range(1,(n-r)+1):
            k=k*i
        s=n1//(r1*k)
        return s%(10**9+7)
            
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends