#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        s=0
        i=0
        j=n-1
        p=1
        q=1
        g,h=-1,-1
        while(s!=2 and i<=n-1 and j>=0):
            if(arr[i]==x and p):
                s+=1
                g=i
                p=0
            if(arr[j]==x and q):
                s+=1
                q=0
                h=j
            if (p):
                i+=1
            if q:
                j-=1
        return g,h





#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends