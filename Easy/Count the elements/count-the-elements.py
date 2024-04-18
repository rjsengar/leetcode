#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        d={}
        l=[]
        b.sort()
    
        for g in query:
            i=a[g]
            k=0
            t=0
            j=0
            s=0
            e=len(b)-1
            m=(s+e)//2 
            while(s<e):
                m=(s+e)//2
                if b[m]==i:
                    k=m
                    t=1
                    break
                if b[m]>i:
                    e=m-1
                if b[m]<i:
                    s=m+1
            if t==0:
                if e<0:
                    k=0
                else:
                    k=e
            while(k<len(b)):
                if b[k]<=i:
                    k+=1
                else:
                    break
            l.append(k)
        return l
                    
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends