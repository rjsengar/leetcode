#User function Template for python3

class Solution:
    def sumOfNaturals(self, n):
        s=0
        s=int((n/2)*(2+(n-1)))
        return s%(10**9+7)





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.sumOfNaturals(n))
# } Driver Code Ends