#User function Template for python3

class Solution:
    def pattern(self, N):
        n=N
        l=[]
        l.append(N)
        while(N>0):
            l.append(N-5)
            N-=5
        while(N+5<=n):
            l.append(N+5)
            N+=5
        return l
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends