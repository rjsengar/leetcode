#User function Template for python3

class Solution:
    def sequence(self, n):
        c=0
        s1=0
        s=0
        k=1
        while(c<n):
            s1=1
            i=0
            while(i<=c):
                s1*=k
                s1=s1%(10**9+7)
                k+=1
                i+=1
            c+=1
            s+=s1
            s=s%(10**9+7)
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends