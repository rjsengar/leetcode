#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        d={}
        d[0]=1
        l=[0]
        m=0
        for i in range(1,n):
            s=m-i
            s1=m+i
            if s<=0:
                s=s1
            if s not in d:
                m=s
            else:
                m=s1
            l.append(m)
            d[m]=1
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends