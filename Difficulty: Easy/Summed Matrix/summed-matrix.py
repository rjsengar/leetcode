#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        i=1
        c=0
        if q<=2*n:
            if n+1>q:
                return q-1
            if n+1==q:
                return n
            else:
                return n-(q-(n+1))
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends