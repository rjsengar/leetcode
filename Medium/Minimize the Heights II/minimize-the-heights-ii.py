#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        l=[]
        arr.sort()
        a=arr[-1]-arr[0]
        for i in range(1,n):
            if(arr[i]-k<0):
                continue
            m1=max(arr[i-1]+k,arr[-1]-k)
            m2=min(arr[i]-k,arr[0]+k)
            a=min(m1-m2,a)
        return a





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends