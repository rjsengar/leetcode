#User function Template for python3


def LargButMinFreq(arr,n):
    m=max(arr)
    s=len(arr)
    m1=min(arr)
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    k=min(d.values())
    for i in arr:
        if d[i]==k:
            if m1<i:
                m1=i
            
    return m1





#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends