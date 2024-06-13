#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        d={}
        if n<3:
            return 1
        a,b=1,1
        c=1
        for i in range(3,n+1):
            a,b,c=b,c,(a+b)%(10**9+7)

        return c%10**(9+7)





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends