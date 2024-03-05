# User Template code

def MaxZero(arr, n):
    m=0
    ma=-1
    for i in arr:
        s=str(i)
        c=s.count('0')
        if c>m:
            ma=i
            m=c
        if c and c==m:
            ma=max(ma,i)
    return ma
            


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a=list(map(int,input().split()))
        print(MaxZero(a,n))
# } Driver Code Ends