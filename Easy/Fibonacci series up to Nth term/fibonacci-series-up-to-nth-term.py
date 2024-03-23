#User function Template for python3
class Solution:
    def series(self, n):
        l=[0,1]
        for i in range(n-1):
            a=l[i]+l[i+1]
            l.append(a%(10**9+7))
        return l
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends