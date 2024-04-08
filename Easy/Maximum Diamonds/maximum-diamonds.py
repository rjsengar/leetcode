#User function Template for python3

import heapq

class Solution:
    def maxDiamonds(self, A, N, K):
        # code here 
        a = [-x for x in A]
        heapq.heapify(a)
        ans = 0
        for x in range (K):
            m = heapq.heappop(a)
            ans+=abs(m)
            m = abs(m)//2
            heapq.heappush(a,-m)
        return ans





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends