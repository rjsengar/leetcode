#User function Template for python3

class Solution:

    def countStr(self, n):
        return (2 + (3 * n) + (n * n * n))//2
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends