#User function Template for python3

class Solution:
    def minxorpair (self, N, arr):
        arr.sort()
        m=100000
        for i in range(N-1):
            if arr[i]^arr[i+1]<m:
                m=arr[i]^arr[i+1]
        return m
        
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
    
        ob = Solution()
        print(ob.minxorpair(N,arr))
        

# } Driver Code Ends