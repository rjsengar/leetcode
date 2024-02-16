#User function Template for python3

class Solution:
    def common_element(self,v1,v2):
        d={}
        for i in v1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i in v2:
            if i in d and d[i]>0:
                l.append(i)
                d[i]-=1
        l.sort()
        return l
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        v1=list(map(int,input().split()))
        m=int(input())
        v2=list(map(int,input().split()))
        ob=Solution()
        ans=ob.common_element(v1, v2);
        for i in ans:
            print(i,end = " ")
        print()
# } Driver Code Ends