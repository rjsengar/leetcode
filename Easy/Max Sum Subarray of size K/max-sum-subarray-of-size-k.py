#User function Template for python3
class Solution:
    def maximumSumSubarray (self,k,arr,n):
        s=0
        for i in range(k):
            s+=arr[i]
        m=s
        i=0
        j=i+k
        while(i<n-k):
            s=s-arr[i]
            s+=arr[j]
            m=max(m,s)
            i+=1
            j+=1
        return m
            
            








#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends